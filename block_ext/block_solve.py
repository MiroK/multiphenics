# Copyright (C) 2016 by the block_ext authors
#
# This file is part of block_ext.
#
# block_ext is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# block_ext is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with block_ext. If not, see <http://www.gnu.org/licenses/>.
#

from block_matrix import BlockMatrix
from block_vector import BlockVector
from monolithic_matrix import MonolithicMatrix

def block_solve(block_A, block_x, block_b):
    assert isinstance(block_A, BlockMatrix)
    assert isinstance(block_x, BlockVector)
    assert isinstance(block_b, BlockVector)
    # Init monolithic matrix/vector corresponding to block matrix/vector
    A = MonolithicMatrix(block_A)
    x, b = A.create_monolithic_vectors(block_x, block_b)
    # Copy values from block matrix/vector to monolithic matrix/vector
    A.zero(); A.block_add(block_A)
    b.zero(); b.block_add(block_b)
    # Solve
    from dolfin import solve
    solve(A, x, b)
    # Move back values from monolithic solution to block vector
    x.copy_values_to(block_x)