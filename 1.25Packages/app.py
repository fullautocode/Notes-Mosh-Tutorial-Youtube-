# 3:30:28

# Packages are directories that contain multiple modules
# To create a package, make a new directory and create a __init__.py file.

# Method 1
import ecommerce.shipping
# import packagename.modulename
 
ecommerce.shipping.calc_shipping()
#packagename.module.function()

# Method 2
from ecommerce.shipping import calc_shipping#, function2, function3
calc_shipping()
# This way the function can be called directly


# Individual Packages can also be imported
from ecommerce import shipping
shipping.calc_shipping()
