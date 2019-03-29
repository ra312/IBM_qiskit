import qiskit

qr = qiskit.QuantumRegister(1)
cr = qiskit.ClassicalRegister(1)
program = qiskit.QuantumCircuit(qr, cr)
program.measure(qr,cr)

job = qiskit.execute( program, qiskit.BasicAer.get_backend('qasm_simulator') )
print( job.result().get_counts() )

my_ibmq_token = '3d11b0e791bf48bfb27b11a133f1f76dc818b873f86fbcb2585407312d1dd23269cd3a2521a14230db84f2c9135f362fd6d55f1be2769c9d7a24a05e73e748aa'
#ibmq_account = qiskit.IBMQ.save_account(my_ibmq_token)
my_ibmq = qiskit.IBMQ.save_account(my_ibmq_token, overwrite=True)
# make sure we have the ibmq account credentials!
print(qiskit.IBMQ.stored_accounts())

qiskit.IBMQ.load_accounts()
#backend = qiskit.providers.ibmq.least_busy(qiskit.IBMQ.backends(simulator=False))
#print("We'll use the least busy device:",backend.name())
#job = qiskit.execute( program, backend )
#print( job.result().get_counts() )
