# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from azure.profiles import KnownProfiles, ProfileDefinition
from azure.profiles.multiapiclient import MultiApiClientMixin
from msrest import Deserializer, Serializer

from ._configuration import ResourceManagementClientConfiguration

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

class _SDKClient(object):
    def __init__(self, *args, **kwargs):
        """This is a fake class to support current implemetation of MultiApiClientMixin."
        Will be removed in final version of multiapi azure-core based client
        """
        pass

class ResourceManagementClient(MultiApiClientMixin, _SDKClient):
    """Provides operations for working with resources and resource groups.

    This ready contains multiple API versions, to help you deal with all of the Azure clouds
    (Azure Stack, Azure Government, Azure China, etc.).
    By default, it uses the latest API version available on public Azure.
    For production, you should stick to a particular api-version and/or profile.
    The profile sets a mapping between an operation group and its API version.
    The api-version parameter sets the default API version if the operation
    group is not described in the profile.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: API version to use if no profile is provided, or if missing in profile.
    :type api_version: str
    :param base_url: Service URL
    :type base_url: str
    :param profile: A profile definition, from KnownProfiles to dict.
    :type profile: azure.profiles.KnownProfiles
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    DEFAULT_API_VERSION = '2021-04-01'
    _PROFILE_TAG = "azure.mgmt.resource.resources.ResourceManagementClient"
    LATEST_PROFILE = ProfileDefinition({
        _PROFILE_TAG: {
            None: DEFAULT_API_VERSION,
        }},
        _PROFILE_TAG + " latest"
    )

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        api_version=None, # type: Optional[str]
        base_url=None,  # type: Optional[str]
        profile=KnownProfiles.default, # type: KnownProfiles
        **kwargs  # type: Any
    ):
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = ResourceManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)
        super(ResourceManagementClient, self).__init__(
            api_version=api_version,
            profile=profile
        )

    @classmethod
    def _models_dict(cls, api_version):
        return {k: v for k, v in cls.models(api_version).__dict__.items() if isinstance(v, type)}

    @classmethod
    def models(cls, api_version=DEFAULT_API_VERSION):
        """Module depends on the API version:

           * 2016-02-01: :mod:`v2016_02_01.models<azure.mgmt.resource.resources.v2016_02_01.models>`
           * 2016-09-01: :mod:`v2016_09_01.models<azure.mgmt.resource.resources.v2016_09_01.models>`
           * 2017-05-10: :mod:`v2017_05_10.models<azure.mgmt.resource.resources.v2017_05_10.models>`
           * 2018-02-01: :mod:`v2018_02_01.models<azure.mgmt.resource.resources.v2018_02_01.models>`
           * 2018-05-01: :mod:`v2018_05_01.models<azure.mgmt.resource.resources.v2018_05_01.models>`
           * 2019-03-01: :mod:`v2019_03_01.models<azure.mgmt.resource.resources.v2019_03_01.models>`
           * 2019-05-01: :mod:`v2019_05_01.models<azure.mgmt.resource.resources.v2019_05_01.models>`
           * 2019-05-10: :mod:`v2019_05_10.models<azure.mgmt.resource.resources.v2019_05_10.models>`
           * 2019-07-01: :mod:`v2019_07_01.models<azure.mgmt.resource.resources.v2019_07_01.models>`
           * 2019-08-01: :mod:`v2019_08_01.models<azure.mgmt.resource.resources.v2019_08_01.models>`
           * 2019-10-01: :mod:`v2019_10_01.models<azure.mgmt.resource.resources.v2019_10_01.models>`
           * 2020-06-01: :mod:`v2020_06_01.models<azure.mgmt.resource.resources.v2020_06_01.models>`
           * 2020-10-01: :mod:`v2020_10_01.models<azure.mgmt.resource.resources.v2020_10_01.models>`
           * 2021-01-01: :mod:`v2021_01_01.models<azure.mgmt.resource.resources.v2021_01_01.models>`
           * 2021-04-01: :mod:`v2021_04_01.models<azure.mgmt.resource.resources.v2021_04_01.models>`
        """
        if api_version == '2016-02-01':
            from .v2016_02_01 import models
            return models
        elif api_version == '2016-09-01':
            from .v2016_09_01 import models
            return models
        elif api_version == '2017-05-10':
            from .v2017_05_10 import models
            return models
        elif api_version == '2018-02-01':
            from .v2018_02_01 import models
            return models
        elif api_version == '2018-05-01':
            from .v2018_05_01 import models
            return models
        elif api_version == '2019-03-01':
            from .v2019_03_01 import models
            return models
        elif api_version == '2019-05-01':
            from .v2019_05_01 import models
            return models
        elif api_version == '2019-05-10':
            from .v2019_05_10 import models
            return models
        elif api_version == '2019-07-01':
            from .v2019_07_01 import models
            return models
        elif api_version == '2019-08-01':
            from .v2019_08_01 import models
            return models
        elif api_version == '2019-10-01':
            from .v2019_10_01 import models
            return models
        elif api_version == '2020-06-01':
            from .v2020_06_01 import models
            return models
        elif api_version == '2020-10-01':
            from .v2020_10_01 import models
            return models
        elif api_version == '2021-01-01':
            from .v2021_01_01 import models
            return models
        elif api_version == '2021-04-01':
            from .v2021_04_01 import models
            return models
        raise ValueError("API version {} is not available".format(api_version))

    @property
    def deployment_operations(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2016_02_01.operations.DeploymentOperationsOperations>`
           * 2016-09-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2016_09_01.operations.DeploymentOperationsOperations>`
           * 2017-05-10: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2017_05_10.operations.DeploymentOperationsOperations>`
           * 2018-02-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2018_02_01.operations.DeploymentOperationsOperations>`
           * 2018-05-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2018_05_01.operations.DeploymentOperationsOperations>`
           * 2019-03-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2019_03_01.operations.DeploymentOperationsOperations>`
           * 2019-05-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2019_05_01.operations.DeploymentOperationsOperations>`
           * 2019-05-10: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2019_05_10.operations.DeploymentOperationsOperations>`
           * 2019-07-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2019_07_01.operations.DeploymentOperationsOperations>`
           * 2019-08-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2019_08_01.operations.DeploymentOperationsOperations>`
           * 2019-10-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2019_10_01.operations.DeploymentOperationsOperations>`
           * 2020-06-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2020_06_01.operations.DeploymentOperationsOperations>`
           * 2020-10-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2020_10_01.operations.DeploymentOperationsOperations>`
           * 2021-01-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2021_01_01.operations.DeploymentOperationsOperations>`
           * 2021-04-01: :class:`DeploymentOperationsOperations<azure.mgmt.resource.resources.v2021_04_01.operations.DeploymentOperationsOperations>`
        """
        api_version = self._get_api_version('deployment_operations')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2019-03-01':
            from .v2019_03_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2019-10-01':
            from .v2019_10_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2020-06-01':
            from .v2020_06_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2020-10-01':
            from .v2020_10_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2021-01-01':
            from .v2021_01_01.operations import DeploymentOperationsOperations as OperationClass
        elif api_version == '2021-04-01':
            from .v2021_04_01.operations import DeploymentOperationsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'deployment_operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def deployments(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2016_02_01.operations.DeploymentsOperations>`
           * 2016-09-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2016_09_01.operations.DeploymentsOperations>`
           * 2017-05-10: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2017_05_10.operations.DeploymentsOperations>`
           * 2018-02-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2018_02_01.operations.DeploymentsOperations>`
           * 2018-05-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2018_05_01.operations.DeploymentsOperations>`
           * 2019-03-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2019_03_01.operations.DeploymentsOperations>`
           * 2019-05-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2019_05_01.operations.DeploymentsOperations>`
           * 2019-05-10: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2019_05_10.operations.DeploymentsOperations>`
           * 2019-07-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2019_07_01.operations.DeploymentsOperations>`
           * 2019-08-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2019_08_01.operations.DeploymentsOperations>`
           * 2019-10-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2019_10_01.operations.DeploymentsOperations>`
           * 2020-06-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2020_06_01.operations.DeploymentsOperations>`
           * 2020-10-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2020_10_01.operations.DeploymentsOperations>`
           * 2021-01-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2021_01_01.operations.DeploymentsOperations>`
           * 2021-04-01: :class:`DeploymentsOperations<azure.mgmt.resource.resources.v2021_04_01.operations.DeploymentsOperations>`
        """
        api_version = self._get_api_version('deployments')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import DeploymentsOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2019-03-01':
            from .v2019_03_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import DeploymentsOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2019-10-01':
            from .v2019_10_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2020-06-01':
            from .v2020_06_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2020-10-01':
            from .v2020_10_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2021-01-01':
            from .v2021_01_01.operations import DeploymentsOperations as OperationClass
        elif api_version == '2021-04-01':
            from .v2021_04_01.operations import DeploymentsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'deployments'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def operations(self):
        """Instance depends on the API version:

           * 2018-05-01: :class:`Operations<azure.mgmt.resource.resources.v2018_05_01.operations.Operations>`
           * 2019-03-01: :class:`Operations<azure.mgmt.resource.resources.v2019_03_01.operations.Operations>`
           * 2019-05-01: :class:`Operations<azure.mgmt.resource.resources.v2019_05_01.operations.Operations>`
           * 2019-05-10: :class:`Operations<azure.mgmt.resource.resources.v2019_05_10.operations.Operations>`
           * 2019-07-01: :class:`Operations<azure.mgmt.resource.resources.v2019_07_01.operations.Operations>`
           * 2019-08-01: :class:`Operations<azure.mgmt.resource.resources.v2019_08_01.operations.Operations>`
           * 2019-10-01: :class:`Operations<azure.mgmt.resource.resources.v2019_10_01.operations.Operations>`
           * 2020-06-01: :class:`Operations<azure.mgmt.resource.resources.v2020_06_01.operations.Operations>`
           * 2020-10-01: :class:`Operations<azure.mgmt.resource.resources.v2020_10_01.operations.Operations>`
           * 2021-01-01: :class:`Operations<azure.mgmt.resource.resources.v2021_01_01.operations.Operations>`
           * 2021-04-01: :class:`Operations<azure.mgmt.resource.resources.v2021_04_01.operations.Operations>`
        """
        api_version = self._get_api_version('operations')
        if api_version == '2018-05-01':
            from .v2018_05_01.operations import Operations as OperationClass
        elif api_version == '2019-03-01':
            from .v2019_03_01.operations import Operations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import Operations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import Operations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import Operations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import Operations as OperationClass
        elif api_version == '2019-10-01':
            from .v2019_10_01.operations import Operations as OperationClass
        elif api_version == '2020-06-01':
            from .v2020_06_01.operations import Operations as OperationClass
        elif api_version == '2020-10-01':
            from .v2020_10_01.operations import Operations as OperationClass
        elif api_version == '2021-01-01':
            from .v2021_01_01.operations import Operations as OperationClass
        elif api_version == '2021-04-01':
            from .v2021_04_01.operations import Operations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'operations'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def provider_resource_types(self):
        """Instance depends on the API version:

           * 2020-10-01: :class:`ProviderResourceTypesOperations<azure.mgmt.resource.resources.v2020_10_01.operations.ProviderResourceTypesOperations>`
           * 2021-01-01: :class:`ProviderResourceTypesOperations<azure.mgmt.resource.resources.v2021_01_01.operations.ProviderResourceTypesOperations>`
           * 2021-04-01: :class:`ProviderResourceTypesOperations<azure.mgmt.resource.resources.v2021_04_01.operations.ProviderResourceTypesOperations>`
        """
        api_version = self._get_api_version('provider_resource_types')
        if api_version == '2020-10-01':
            from .v2020_10_01.operations import ProviderResourceTypesOperations as OperationClass
        elif api_version == '2021-01-01':
            from .v2021_01_01.operations import ProviderResourceTypesOperations as OperationClass
        elif api_version == '2021-04-01':
            from .v2021_04_01.operations import ProviderResourceTypesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'provider_resource_types'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def providers(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2016_02_01.operations.ProvidersOperations>`
           * 2016-09-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2016_09_01.operations.ProvidersOperations>`
           * 2017-05-10: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2017_05_10.operations.ProvidersOperations>`
           * 2018-02-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2018_02_01.operations.ProvidersOperations>`
           * 2018-05-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2018_05_01.operations.ProvidersOperations>`
           * 2019-03-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2019_03_01.operations.ProvidersOperations>`
           * 2019-05-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2019_05_01.operations.ProvidersOperations>`
           * 2019-05-10: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2019_05_10.operations.ProvidersOperations>`
           * 2019-07-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2019_07_01.operations.ProvidersOperations>`
           * 2019-08-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2019_08_01.operations.ProvidersOperations>`
           * 2019-10-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2019_10_01.operations.ProvidersOperations>`
           * 2020-06-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2020_06_01.operations.ProvidersOperations>`
           * 2020-10-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2020_10_01.operations.ProvidersOperations>`
           * 2021-01-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2021_01_01.operations.ProvidersOperations>`
           * 2021-04-01: :class:`ProvidersOperations<azure.mgmt.resource.resources.v2021_04_01.operations.ProvidersOperations>`
        """
        api_version = self._get_api_version('providers')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import ProvidersOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2019-03-01':
            from .v2019_03_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import ProvidersOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2019-10-01':
            from .v2019_10_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2020-06-01':
            from .v2020_06_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2020-10-01':
            from .v2020_10_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2021-01-01':
            from .v2021_01_01.operations import ProvidersOperations as OperationClass
        elif api_version == '2021-04-01':
            from .v2021_04_01.operations import ProvidersOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'providers'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def resource_groups(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2016_02_01.operations.ResourceGroupsOperations>`
           * 2016-09-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2016_09_01.operations.ResourceGroupsOperations>`
           * 2017-05-10: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2017_05_10.operations.ResourceGroupsOperations>`
           * 2018-02-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2018_02_01.operations.ResourceGroupsOperations>`
           * 2018-05-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2018_05_01.operations.ResourceGroupsOperations>`
           * 2019-03-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2019_03_01.operations.ResourceGroupsOperations>`
           * 2019-05-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2019_05_01.operations.ResourceGroupsOperations>`
           * 2019-05-10: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2019_05_10.operations.ResourceGroupsOperations>`
           * 2019-07-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2019_07_01.operations.ResourceGroupsOperations>`
           * 2019-08-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2019_08_01.operations.ResourceGroupsOperations>`
           * 2019-10-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2019_10_01.operations.ResourceGroupsOperations>`
           * 2020-06-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2020_06_01.operations.ResourceGroupsOperations>`
           * 2020-10-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2020_10_01.operations.ResourceGroupsOperations>`
           * 2021-01-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2021_01_01.operations.ResourceGroupsOperations>`
           * 2021-04-01: :class:`ResourceGroupsOperations<azure.mgmt.resource.resources.v2021_04_01.operations.ResourceGroupsOperations>`
        """
        api_version = self._get_api_version('resource_groups')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2019-03-01':
            from .v2019_03_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2019-10-01':
            from .v2019_10_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2020-06-01':
            from .v2020_06_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2020-10-01':
            from .v2020_10_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2021-01-01':
            from .v2021_01_01.operations import ResourceGroupsOperations as OperationClass
        elif api_version == '2021-04-01':
            from .v2021_04_01.operations import ResourceGroupsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'resource_groups'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def resources(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2016_02_01.operations.ResourcesOperations>`
           * 2016-09-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2016_09_01.operations.ResourcesOperations>`
           * 2017-05-10: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2017_05_10.operations.ResourcesOperations>`
           * 2018-02-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2018_02_01.operations.ResourcesOperations>`
           * 2018-05-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2018_05_01.operations.ResourcesOperations>`
           * 2019-03-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2019_03_01.operations.ResourcesOperations>`
           * 2019-05-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2019_05_01.operations.ResourcesOperations>`
           * 2019-05-10: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2019_05_10.operations.ResourcesOperations>`
           * 2019-07-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2019_07_01.operations.ResourcesOperations>`
           * 2019-08-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2019_08_01.operations.ResourcesOperations>`
           * 2019-10-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2019_10_01.operations.ResourcesOperations>`
           * 2020-06-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2020_06_01.operations.ResourcesOperations>`
           * 2020-10-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2020_10_01.operations.ResourcesOperations>`
           * 2021-01-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2021_01_01.operations.ResourcesOperations>`
           * 2021-04-01: :class:`ResourcesOperations<azure.mgmt.resource.resources.v2021_04_01.operations.ResourcesOperations>`
        """
        api_version = self._get_api_version('resources')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import ResourcesOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2019-03-01':
            from .v2019_03_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import ResourcesOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2019-10-01':
            from .v2019_10_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2020-06-01':
            from .v2020_06_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2020-10-01':
            from .v2020_10_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2021-01-01':
            from .v2021_01_01.operations import ResourcesOperations as OperationClass
        elif api_version == '2021-04-01':
            from .v2021_04_01.operations import ResourcesOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'resources'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    @property
    def tags(self):
        """Instance depends on the API version:

           * 2016-02-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2016_02_01.operations.TagsOperations>`
           * 2016-09-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2016_09_01.operations.TagsOperations>`
           * 2017-05-10: :class:`TagsOperations<azure.mgmt.resource.resources.v2017_05_10.operations.TagsOperations>`
           * 2018-02-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2018_02_01.operations.TagsOperations>`
           * 2018-05-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2018_05_01.operations.TagsOperations>`
           * 2019-03-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2019_03_01.operations.TagsOperations>`
           * 2019-05-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2019_05_01.operations.TagsOperations>`
           * 2019-05-10: :class:`TagsOperations<azure.mgmt.resource.resources.v2019_05_10.operations.TagsOperations>`
           * 2019-07-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2019_07_01.operations.TagsOperations>`
           * 2019-08-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2019_08_01.operations.TagsOperations>`
           * 2019-10-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2019_10_01.operations.TagsOperations>`
           * 2020-06-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2020_06_01.operations.TagsOperations>`
           * 2020-10-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2020_10_01.operations.TagsOperations>`
           * 2021-01-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2021_01_01.operations.TagsOperations>`
           * 2021-04-01: :class:`TagsOperations<azure.mgmt.resource.resources.v2021_04_01.operations.TagsOperations>`
        """
        api_version = self._get_api_version('tags')
        if api_version == '2016-02-01':
            from .v2016_02_01.operations import TagsOperations as OperationClass
        elif api_version == '2016-09-01':
            from .v2016_09_01.operations import TagsOperations as OperationClass
        elif api_version == '2017-05-10':
            from .v2017_05_10.operations import TagsOperations as OperationClass
        elif api_version == '2018-02-01':
            from .v2018_02_01.operations import TagsOperations as OperationClass
        elif api_version == '2018-05-01':
            from .v2018_05_01.operations import TagsOperations as OperationClass
        elif api_version == '2019-03-01':
            from .v2019_03_01.operations import TagsOperations as OperationClass
        elif api_version == '2019-05-01':
            from .v2019_05_01.operations import TagsOperations as OperationClass
        elif api_version == '2019-05-10':
            from .v2019_05_10.operations import TagsOperations as OperationClass
        elif api_version == '2019-07-01':
            from .v2019_07_01.operations import TagsOperations as OperationClass
        elif api_version == '2019-08-01':
            from .v2019_08_01.operations import TagsOperations as OperationClass
        elif api_version == '2019-10-01':
            from .v2019_10_01.operations import TagsOperations as OperationClass
        elif api_version == '2020-06-01':
            from .v2020_06_01.operations import TagsOperations as OperationClass
        elif api_version == '2020-10-01':
            from .v2020_10_01.operations import TagsOperations as OperationClass
        elif api_version == '2021-01-01':
            from .v2021_01_01.operations import TagsOperations as OperationClass
        elif api_version == '2021-04-01':
            from .v2021_04_01.operations import TagsOperations as OperationClass
        else:
            raise ValueError("API version {} does not have operation group 'tags'".format(api_version))
        return OperationClass(self._client, self._config, Serializer(self._models_dict(api_version)), Deserializer(self._models_dict(api_version)))

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
