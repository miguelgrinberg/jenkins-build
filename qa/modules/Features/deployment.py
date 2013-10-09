"""
A Deployment Features
"""

from feature import Feature

class Deployment(Feature):
    """ Represents a feature across a deployment
    """

    def __init__(self, deployment):
        super(Deployment, self).__init__(deployment.config)
        self.deployment = deployment

    def update_environment(self):
        pass


#############################################################################
############################ OpenStack Features #############################
#############################################################################

class OpenStack(Deployment):
    """ Represents a Rackspace Private Cloud Software Feature
    """

    def __init__(self, deployment):
        super(OpenStack, self).__init__(deployment)

    def update_environment(self):
        pass

class Neutron(Deployment):
    """ Represents a neutron network cluster
    """

    def __init__(self, deployment, rpcs_feature):
        super(Neutron, self).__init__(deployment)
        self.environment = \
            self.config['environments'][self.__name__.lower()][rpcs_feature]

    def update_environment(self):
        self.node.environment.add_override_attr('neutron', self.environment)


class Swift(Deployment):
    """ Represents a block storage cluster enabled by swift
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Swift, self).__init__(deployment)
        self.environment = \
            self.config['environments'][self.__name__.lower()][rpcs_feature]

    def update_environment(self):
        self.node.environment.add_override_attr(
            self.__name__.lower(), self.environment)


class Glance(Deployment):
    """ Represents a glance with cloud files backend
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Glance, self).__init__(deployment)
        self.environment = \
            self.config['environment'][self.__name__.lower()][rpcs_feature]

    def update_environment(self):
        self.node.environment.add_override_attr(
            self.__name__.lower(), self.environment)


class Keystone(Deployment):
    """ Represents the keystone feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Keystone, self).__init__(deployment)
        self.environment = \
            self.config['environments'][self.__name__.lower()][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.__name__.lower(), self.environment)


class Nova(Deployment):
    """ Represents the monitoring feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Monitoring, self).__init__(deployment)
        self.environment = \
            self.config['environments'][self.__name__.lower()][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.__name__.lower(), self.environment)


class Horizon(Deployment):
    """ Represents the monitoring feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Monitoring, self).__init__(deployment)
        self.environment = \
            self.config['environments'][self.__name__.lower()][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.__name__.lower(), self.environment)

class Cinder(Deployment):
    """ Represents the Cinder feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Cinder, self).__init__(deployment)
        self.environment = \
            self.config['environments'][self.__name__.lower()][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.__name__.lower(), self.environment)


#############################################################################
############### Rackspace Private Cloud Software Features ###################
#############################################################################

class RPCS(Deployment):
    """ Represents a Rackspace Private Cloud Software Feature
    """

    def __init__(self, deployment, name):
        super(RPCS, self).__init__(deployment)
        self.name = name

    def update_environment(self):
        pass

class Monitoring(RPCS):
    """ Represents the monitoring feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Monitoring, self).__init__(deployment,
                                         self.__name__.lower())
        self.environment = \
            self.config['environments'][self.name][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.__name__.lower(), self.environment)

class MySql(RPCS):
    """ Represents the monitoring feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Monitoring, self).__init__(deployment,
                                         self.__name__.lower())
        self.environment = \
            self.config['environments'][self.name][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.name, self.environment)


class OsOps(RPCS):
    """ Represents the monitoring feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Monitoring, self).__init__(deployment,
                                         self.__name__.lower())
        self.environment = \
            self.config['environments'][self.name][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.name, self.environment)


class DeveloperMode(RPCS):
    """ Represents the monitoring feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Monitoring, self).__init__(deployment, 'developer_mode')
        self.environment = \
            self.config['environments'][self.name][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.name, self.environment)


class OsOpsNetworks(RPCS):
    """ Represents the monitoring feature
    """

    def __init__(self, deployment, rpcs_feature='default'):
        super(Monitoring, self).__init__(deployment, 'osops_networks')
        self.environment = \
            self.config['environments'][self.name][rpcs_feature]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.name, self.environment)


class HighAvailability(RPCS):
    """ Represents a highly available cluster
    """

    def __init__(self, deployment):
        super(HighAvailability, self).__init__(deployment, 'ha')
        self.environment = \
            self.config['environments'][self.name][deployment.os]

    def update_environment(self):
        self.node.environment.add_override_attr(self.name, self.environment)


class LDAP(RPCS):
    """ Represents a keystone with an openldap backend
    """

    def __init__(self, deployment):
        super(LDAP, self).__init__(deployment,
                                   self.__name__.lower())
        self.environment = \
            self.config['environments'][self.name]

    def update_environment(self):
        self.deployment.environment.add_override_attr(
            self.name, self.environment)