from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import numpy as np
import logging, random, math, string

logging.getLogger("qiskit").setLevel(logging.WARNING)


def _entropy_simulation_(seed: int):
    np.random.seed(seed % 1337)
    garbage_data = [np.sin(seed) ** 2 for _ in range(10)]
    np.random.shuffle(garbage_data)
    return sum(garbage_data) * 136

def _quantum_gate_rotation_(qc):
    qc.x(0)
    qc.x(0)  
    qc.rz(2 * np.pi, 0)  
    return qc

def _calculate_noise_parameters_(x):
    return ((x ** 3 - x ** 2) * random.random())  

noop = lambda *a, **k: None  

def _anti_optimizer_padding_():
    s = 0
    for i in range(3):
        s += (i ** 8 - i ** 7)
    if s == 42:
        print("Quantum collapse detected!")  
    return s


def quantum_entanglement(flag):
    sim = AerSimulator()
    outputs = []
    n = len(flag)

    _anti_optimizer_padding_()

    for i in range(n - 1):
        a = ord(flag[i])
        b = ord(flag[i + 1])
        phase = (a * 13 + b * 19 + i * 11) % 360
        amp = ((a ^ b) + 10) / 100.0

        _entropy_simulation_(a + b + i)
        _calculate_noise_parameters_(a * b)
        
        qc = QuantumCircuit(1, 1)
        qc.ry(amp * np.pi, 0)
        qc.rz(np.radians(phase), 0)

        _quantum_gate_rotation_(qc)
        qc.barrier()

        qc.measure(0, 0)
        qc.measure_all(add_bits=False)

        tqc = transpile(qc, sim, optimization_level=0)

        job = sim.run(tqc, shots=500, seed_simulator=a + 1000*b + i*7)
        res = job.result()

        try:
            counts = res.get_counts()
        except Exception:
            data_block = res.data(0)
            counts = data_block.get("counts", {})

        p1 = counts.get('1', 0) / 500.0 if counts else 0.0
        outputs.append(round(p1, 5))

        noop(random.random(), math.exp(0), string.ascii_letters)

    return outputs


if __name__ == "__main__":
    flag = # "figure it out"
    print("Quantum device measurement outputs:", flush=True)
    print(quantum_entanglement(flag), flush=True)
