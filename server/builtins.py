from elizabeth import Generic
from elizabeth.builtins import (
    RussiaSpecProvider,
    BrazilSpecProvider,
    JapanSpecProvider,
    USASpecProvider
)


def add_builtins(generic: Generic) -> Generic:
    """Add builtins specific providers to Generic provider.
    
    Args:
        generic: An instance of Generic.
    
    Returns:
        Generic which support specific providers.
    """
    if isinstance(generic, Generic):
        generic.add_provider(RussiaSpecProvider)
        generic.add_provider(BrazilSpecProvider)
        generic.add_provider(JapanSpecProvider)
        generic.add_provider(USASpecProvider)
        return generic
    else:
        raise TypeError("Provider must be a class")
