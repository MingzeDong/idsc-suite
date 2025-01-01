==============
SIMVI
==============

SimVI Model
-----------

.. autoclass:: simvi.model.simvi.SimVIModel
   :no-members:
   :show-inheritance:

Methods Table
~~~~~~~~~~~~~
.. autosummary::
   :nosignatures:

   simvi.model.simvi.SimVIModel.setup_anndata
   simvi.model.simvi.SimVIModel.extract_edge_index
   simvi.model.simvi.SimVIModel.train
   simvi.model.simvi.SimVIModel.get_latent_representation
   simvi.model.simvi.SimVIModel.get_attention
   simvi.model.simvi.SimVIModel.get_archetypes
   simvi.model.simvi.SimVIModel.get_se

Preprocessing
~~~~~~~~~~~~~

.. automethod:: simvi.model.simvi.SimVIModel.setup_anndata
.. autofunction:: simvi.model.simvi.SimVIModel.extract_edge_index

Training
~~~~~~~~~~~~~

.. automethod:: simvi.model.simvi.SimVIModel.train

Post-Training / Inference
~~~~~~~~~~~~~

.. automethod:: simvi.model.simvi.SimVIModel.get_latent_representation
.. automethod:: simvi.model.simvi.SimVIModel.get_attention
.. automethod:: simvi.model.simvi.SimVIModel.get_archetypes
.. automethod:: simvi.model.simvi.SimVIModel.get_se

Helper Functions
~~~~~~~~~~~~~~

.. autofunction:: simvi.model.simvi._train
.. autofunction:: simvi.model.simvi._eval
.. autofunction:: simvi.model.simvi.return_f_pv
