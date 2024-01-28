sphinx-apidoc -o . ..
# Update models.rst
echo "Models Module
=============

This module contains the definition of models used in the Mouhami-DZ application.

.. module:: models

   This module defines the following models:

User Model
~~~~~~~~~~

Represents the user in the system.

.. autoclass:: User
   :members:
   :undoc-members:
   :show-inheritance:

Language Model
~~~~~~~~~~~~~~

Represents the languages used in the system.

.. autoclass:: Language
   :members:
   :undoc-members:
   :show-inheritance:

Specialities Model
~~~~~~~~~~~~~~~~~~

Represents the specialities of lawyers in the system.

.. autoclass:: Specialities
   :members:
   :undoc-members:
   :show-inheritance:

Review Model
~~~~~~~~~~~~

Represents the reviews given by users for lawyers in the system.

.. autoclass:: Review
   :members:
   :undoc-members:
   :show-inheritance:

Lawyer Model
~~~~~~~~~~~~

Represents the lawyers in the system.

.. autoclass:: Lawyer
   :members:
   :undoc-members:
   :show-inheritance:

Booking Model
~~~~~~~~~~~~~

Represents the bookings made by users with lawyers in the system.

.. autoclass:: Booking
   :members:
   :undoc-members:
   :show-inheritance:" > models.rst

# Update serializers.rst
echo "Serializers Module
====================

This module contains the serializers configurations for the Mouhami-DZ application.

.. module:: serializers

   This module defines the following serializers:

   - :class:\`LawyerSerializer\`
   - :class:\`BookingSerializer\`
   - :class:\`ReviewSerializer\`
   - :class:\`UserSerializer\`
   - :class:\`LanguageSerializer\`
   - :class:\`SpecialitiesSerializer\`
   - :class:\`LawyerRegistrationSerializer\`
   - :class:\`UserRegistrationSerializer\`

   .. autoclass:: LawyerSerializer
      :members:

   .. autoclass:: BookingSerializer
      :members:

   .. autoclass:: ReviewSerializer
      :members:

   .. autoclass:: UserSerializer
      :members:

   .. autoclass:: LanguageSerializer
      :members:

   .. autoclass:: SpecialitiesSerializer
      :members:

   .. autoclass:: LawyerRegistrationSerializer
      :members:

   .. autoclass:: UserRegistrationSerializer
      :members:" > serializers.rst

# Update urls.rst
echo "URLs Module
===========

This module contains the URL configurations for the Mouhami-DZ application.

.. module:: urls

   This module defines the following URL patterns:

   - ``/lawyers/``: Endpoint for retrieving a list of lawyers.
   - ``/lawyer-detailed/<int:id>``: Endpoint for retrieving detailed information about a specific lawyer.
   - ``/lawyer-booking/<int:id>/bookings/``: Endpoint for making bookings with a specific lawyer.
   - ``/import-lawyers/``: Endpoint for importing lawyer data.
   - ``/mybookingsuser/``: Endpoint for retrieving bookings made by a user.
   - ``/mybookingslawyer/``: Endpoint for retrieving bookings made with a lawyer.
   - ``/search-lawyers``: Endpoint for searching lawyers.
   - ``/login/``: Endpoint for user login.
   - ``/register/``: Endpoint for user registration.
   - ``/register-lawyer/``: Endpoint for lawyer registration.

   .. code-block:: python

      urlpatterns = [
          path('lawyers/', LawyerViewSet.as_view()),
          path('lawyer-detailed/<int:id>', lawyerapi),
          path('lawyer-booking/<int:id>/bookings/', booking),
          path('import-lawyers/', lawyerData),
          path('mybookingsuser/', mybookingsuser),
          path('mybookingslawyer/', mybookingslawyer),
          path('search-lawyers', searchLawyer),
          path('login/', login_view),
          path('register/', UserRegistrationView.as_view()),
          path('register-lawyer/', AvocatRegistrationView.as_view()),
      ]" > urls.rst

# Update views.rst
echo "Views Module
============

This module contains the views implemented in the Mouhami-DZ application.

.. module:: views

   This module defines the following views:

   - :func:\`LawyerViewSet\`: A viewset for retrieving a list of lawyers.
   - :func:\`lawyerapi\`: A view for retrieving detailed information about a specific lawyer.
   - :func:\`booking\`: A view for making bookings with a specific lawyer.
   - :func:\`mybookingslawyer\`: A view for retrieving bookings made by a lawyer.
   - :func:\`mybookingsuser\`: A view for retrieving bookings made by a user.
   - :func:\`lawyerData\`: A view for importing lawyer data.
   - :func:\`searchLawyer\`: A view for searching lawyers.
   - :func:\`generate_access_token\`: A function for generating access tokens.
   - :func:\`generate_refresh_token\`: A function for generating refresh tokens.
   - :class:\`UserRegistrationView\`: A view for user registration.
   - :class:\`AvocatRegistrationView\`: A view for lawyer registration.
   - :func:\`login_view\`: A view for user login.

   .. py:function:: LawyerViewSet

      A viewset for retrieving a list of lawyers.

   .. py:function:: lawyerapi

      A view for retrieving detailed information about a specific lawyer.

   .. py:function:: booking

      A view for making bookings with a specific lawyer.

   .. py:function:: mybookingslawyer

      A view for retrieving bookings made by a lawyer.

   .. py:function:: mybookingsuser

      A view for retrieving bookings made by a user.

   .. py:function:: lawyerData

      A view for importing lawyer data.

   .. py:function:: searchLawyer

      A view for searching lawyers.

   .. py:function:: generate_access_token

      A function for generating access tokens.

   .. py:function:: generate_refresh_token

      A function for generating refresh tokens.

   .. py:class:: UserRegistrationView

      A view for user registration.

   .. py:class:: AvocatRegistrationView

      A view for lawyer registration.

   .. py:function:: login_view

      A view for user login." > views.rst


echo "
.. sds documentation master file, created by
   sphinx-quickstart on Sun Jan 28 21:12:48 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root \`toctree\` directive.

Welcome to sds's documentation!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules/models
   modules/serializers
   modules/urls
   modules/views

Indices and tables
==================

* :ref:\`genindex\`
* :ref:\`modindex\`
* :ref:\`search\`

" > index.rst
