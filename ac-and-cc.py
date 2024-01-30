from tespy.networks import Network
from tespy.components import (Sink, Source, Compressor, CombustionChamber)
from tespy.connections import Connection, Bus

# fluids
air = {'O2': 0.21, 'N2': 0.79}
fuel = {'CH4': 1}

# network
combustion = Network(T_unit='C', p_unit='bar', h_unit='kJ / kg', m_unit='kg / s')

# components
src_air = Source('air-source')
src_fuel = Source('fuel-source')
snk_fluegas = Sink('flue-gas-sink')
cmp_ac = Compressor('air compressor')
cmp_cc = CombustionChamber('combustion chamber')

# connection
c01 = Connection(src_air, 'out1', cmp_ac, 'in1')
c02 = Connection(cmp_ac, 'out1', cmp_cc, 'in1')
c03 = Connection(src_fuel, 'out1', cmp_cc, 'in2')
c04 = Connection(cmp_cc, 'out1', snk_fluegas, 'in1')

combustion.add_conns(c01, c02, c03, c04)

# parameters

# components
cmp_ac.set_attr(eta_s=0.8)
cmp_cc.set_attr(lamb=1.05)

# connections
c01.set_attr(p=1, T=25, fluid=air)
c03.set_attr(p=3, m=1, T=25, fluid=fuel)

# busses
motor_ac = Bus('motor-for-air-compression')
motor_ac.add_comps({'comp': cmp_ac, 'char': 0.975, 'base': 'bus'})

combustion.add_busses(motor_ac)

# solve
combustion.solve(mode='design')
combustion.print_results()
