# Processor REST API
Attempting to build a RESTFUL API using Django Rest Framework, centered around computer processors.

# Before you get started
- Basic Python/Django knowledge 
- Understanding of HTTP/S requests (GET, POST, PUT, PATCH, DELETE)
- Understanding of relational database modelling / Django Model API

# Screens

### Root

![Root View Image](https://github.com/danielc92/django-processor-restapi/blob/master/screens/api-root.jpg)

### Manufacturer List

![Manufacturer List Image](https://github.com/danielc92/django-processor-restapi/blob/master/screens/manufacturer-list.jpg)

### Product Series List

![Product Series List Image](https://github.com/danielc92/django-processor-restapi/blob/master/screens/product-series-list.jpg)

### Processor List

![Processor List Image](https://github.com/danielc92/django-processor-restapi/blob/master/screens/processor-list.jpg)

# Setup
**How to obtain this repository:**
```sh
git clone https://github.com/danielc92/django-processor-restapi.git
```
**Modules/dependencies:**
- `Django==2.2.2`
- `djangorestframework==3.9.4`

# Tests
- Tested inserting data via API
- Tested querying data via API
- Tested pagination of data retrieved via API
- Tested inserting, querying and updating data via Admin Route
- There seems to be an issue with parsing DecimalFields (they show up as strings in JSON response)

# Contributors
- Daniel Corcoran

# Sources
- [Django Rest Framework Documentation](https://www.django-rest-framework.org/tutorial/quickstart/)
