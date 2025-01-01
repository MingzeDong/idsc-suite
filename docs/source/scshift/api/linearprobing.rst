=======================
Linear Probing
=======================

LPModel
-------
.. autoclass:: scshift.LPModel
   :no-members:
   :show-inheritance:

Methods Table
~~~~~~~~~~~~~
.. autosummary::
   :nosignatures:

   scshift.LPModel.train
   scshift.LPModel.predict

Training
~~~~~~~~
.. automethod:: scshift.LPModel.train

Inference
~~~~~~~~~
.. automethod:: scshift.LPModel.predict

Probing Modules
~~~~~~~~~~~~~~~
.. autoclass:: pertvi.model.linearprob.WeightedLinearProbing
   :members:

.. autoclass:: pertvi.model.linearprob.WeightedDisentangledLinearProbing
   :members:

.. autoclass:: pertvi.model.linearprob.ContrastLinearProbing
   :members:

.. autoclass:: pertvi.model.linearprob.LinearProbing
   :members: