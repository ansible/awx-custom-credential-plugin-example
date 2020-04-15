import collections

CredentialPlugin = collections.namedtuple('CredentialPlugin', ['name', 'inputs', 'backend'])

def some_lookup_function(**kwargs):
    #
    # IMPORTANT:
    # replace this section of code with Python code that *actually*
    # interfaces with some third party credential system
    # (*this* code is just provided for the sake of example)
    #
    url = kwargs.get('url')
    token = kwargs.get('token')
    identifier = kwargs.get('identifier')

    if token != 'VALID':
        raise ValueError('Invalid token!')

    value = {
        'username': 'mary',
        'email': 'mary@example.org',
        'password': 'super-secret'
    }

    if identifier in value:
        return value[identifier]

    raise ValueError(f'Could not find a value for {identifier}.')

example_plugin = CredentialPlugin(
    'Example AWX Credential Plugin',
    # see: https://docs.ansible.com/ansible-tower/latest/html/userguide/credential_types.html
    # inputs will be used to create a new CredentialType() instance
    #
    # inputs.fields represents fields the user will specify *when they create*
    # a credential of this type; they generally represent fields
    # used for authentication (URL to the credential management system, any
    # fields necessary for authentication, such as an OAuth2.0 token, or
    # a username and password). They're the types of values you set up _once_
    # in AWX
    #
    # inputs.metadata represents values the user will specify *every time
    # they link two credentials together*
    # this is generally _pathing_ information about _where_ in the external
    # management system you can find the value you care about i.e.,
    #
    # "I would like Machine Credential A to retrieve its username using
    # Credential-O-Matic B at identifier=some_key"
    inputs={
        'fields': [{
            'id': 'url',
            'label': 'Server URL',
            'type': 'string',
        }, {
            'id': 'token',
            'label': 'Authentication Token',
            'type': 'string',
            'secret': True,
        }],
        'metadata': [{
            'id': 'identifier',
            'label': 'Identifier',
            'type': 'string',
            'help_text': 'The name of the key in My Credential System to fetch.'
        }],
        'required': ['url', 'token', 'secret_key'],
    },
    # backend is a callable function which will be passed all of the values
    # defined in `inputs`; this function is responsible for taking the arguments,
    # interacting with the third party credential management system in question
    # using Python code, and returning the value from the third party
    # credential management system
    backend = some_lookup_function
)
