# Copyright (C) 2016-2017 by the multiphenics authors
#
# This file is part of multiphenics.
#
# multiphenics is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# multiphenics is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with multiphenics. If not, see <http://www.gnu.org/licenses/>.
#

from dolfin import as_backend_type, has_pybind11
from multiphenics.python import cpp

if has_pybind11():
    BlockMATLABExport = cpp.la.BlockMATLABExport
else:
    BlockMATLABExport = cpp.BlockMATLABExport

def block_matlab_export(block_tensor, name_tensor):
    BlockMATLABExport.export_(as_backend_type(block_tensor), name_tensor)
