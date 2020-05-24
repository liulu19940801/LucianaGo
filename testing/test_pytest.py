#!/usr/bin/env python
# -*- coding: utf-8 -*-
# type hints 类型提示
import pytest
import self as self
import yaml

from testfunctoion.calc import Calc
from decimal import *


class TestCalc:
    def setup(self):
        self.calc = Calc()
        # self.add_data = yaml.safe_load(open('../testdata/add_data.yaml'))
        # self.div_data = yaml.safe_load(open('../testdata/div_data.yaml'))

    @pytest.mark.add
    @pytest.mark.parametrize("a,b,r", yaml.safe_load(open('../testdata/add_data.yml'))['norm_data'])
    def test_add_normal(self, a, b, r):
        result = self.calc.add(a, b)
        print(result)
        assert result == r

    @pytest.mark.add
    @pytest.mark.xfail
    @pytest.mark.parametrize("a,b,r", yaml.safe_load(open('../testdata/add_data.yml'))['except_data'])
    def test_add_except(self, a, b, r):
        result = self.calc.add(a, b)
        raise TypeError

    @pytest.mark.div
    @pytest.mark.parametrize(["a", "b", "r"], yaml.safe_load(open('../testdata/div_data.yml'))['normal_data'])
    def test_div_normal(self, a, b, r):
        result = self.calc.div(a, b)
        # with pytest.raises('ZeroDivisionError')
        assert result == r

    @pytest.mark.div
    @pytest.mark.xfail
    @pytest.mark.parametrize(("a", "b", "r"), yaml.safe_load(open('../testdata/div_data.yml'))['except_data'])
    def test_div_except(self, a, b, r):
        with pytest.raises(ZeroDivisionError):
            result = self.calc.div(a, b)
        assert result == r


if __name__ == '__main__':
    pytest.main(['-vs','test_pytest.py', '-m div'])
