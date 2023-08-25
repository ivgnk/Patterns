'''
На основе https://refactoring.guru/ru/design-patterns/factory-method

2009 Абстрактные классы и интерфейсы в Питоне https://habr.com/ru/articles/72757/

Разница между абстрактным классом и интерфейсом в Python
2010-2021 https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
2022 https://www.geeksforgeeks.org/difference-between-abstract-class-and-interface-in-python/
2023 https://sky.pro/media/raznicza-mezhdu-abstraktnym-klassom-i-interfejsom-v-python/
В Python разница между абстрактным классом и интерфейсом довольно размыта,
так как оба они реализуются с использованием механизма абстрактных классов.
Однако важно понимать, что принципиальное отличие между ними заключается в том,
что абстрактный класс может иметь как абстрактные, так и неабстрактные методы,
тогда как интерфейс содержит только абстрактные методы.
Следовательно, абстрактный класс можно использовать
для создания общей функциональности для группы связанных классов,
а интерфейс — для определения общего поведения группы классов,
возможно, не связанных между собой.

'''
import inspect
import numpy as np
from bp_const import *
from dataclasses import dataclass

@dataclass
class TheTimeSeries:
    ttime:np.ndarray
    dat:np.ndarray


@dataclass
class TheNamedTimeSeries(TheTimeSeries):
    name: str

class NamedArea:
    type_of_area: str
    name: str
    def __init__(self, ttype_of_area: str, nname:str):
        self.type_of_area = ttype_of_area
        self.name = nname

    def print(self):
        print(self.type_of_area, ' = ', self.name)

class TheRegion(NamedArea):
    def __init__(self, name: str):
        super().__init__(ttype_of_area = 'Region', nname=name)

    def print(self):
        super().print()

class TheCountry(NamedArea):
    iso_short_name:str
    def __init__(self,  name: str, iso_name:str):
        super().__init__(ttype_of_area = 'Country', nname = name)
        self.iso_short_name = iso_name

    def print(self):
        super().print()
        print('ISO Short Name = ', self.iso_short_name)

class TheData:
    country:TheCountry
    region:TheRegion # from spec_region_list
    data: TheNamedTimeSeries

    def __init__(self, cntr: TheCountry, reg: TheRegion, dat: TheNamedTimeSeries):
        self.country = cntr
        self.region = reg
        self.data = dat

    def print(self):
        print('Class name = ',self.__class__.__name__)
        # print(self.__name__)
        # print(inspect.currentframe().f_code.co_name)
        # print('Country = ',self.country.name,', ISO Short Name = ',self.country.iso_short_name)
        # print('Region = ', self.region.name)
        self.country.print()
        self.region.print()

        # печать дата класса
        print('Тип данных =', self.data.name)
        llen = np.size(self.data.ttime)
        for i in range(llen):
            print(self.data.ttime[i],' ',self.data.dat[i])

the_SAU_data = TheNamedTimeSeries(ttime = np.array(oil_gas_prod_years),
                                  dat = np.array(SAU_oilprod_kbd),
                                  name='SAU_oilprod_kbd')
the_SAU = TheData(cntr=TheCountry(name='Saudi Arabia',iso_name='SAU'),
                  reg=TheRegion(name='Middle East'),
                  dat=the_SAU_data)
the_SAU.print()