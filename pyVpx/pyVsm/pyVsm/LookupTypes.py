# ******* WARNING - AUTO GENERATED CODE - DO NOT EDIT *******
from .VmomiSupport import CreateDataType, CreateManagedType
from .VmomiSupport import CreateEnumType
from .VmomiSupport import AddVersion, AddVersionParent
from .VmomiSupport import AddBreakingChangesInfo
from .VmomiSupport import F_LINK, F_LINKABLE
from .VmomiSupport import F_OPTIONAL, F_SECRET
from .VmomiSupport import newestVersions, stableVersions
from .VmomiSupport import publicVersions, dottedVersions
from .VmomiSupport import oldestVersions

AddVersion("lookup.version.version1", "lookup", "1.0", 0, "")
AddVersion("vmodl.version.version0", "", "", 0, "vim25")
AddVersion("vmodl.version.version1", "", "", 0, "vim25")
AddVersion("vmodl.version.version2", "", "", 0, "vim25")
AddVersion("lookup.version.version1_5", "lookup", "version1_5", 0, "")
AddVersion("lookup.version.version2", "lookup", "2.0", 0, "")
AddVersion("lookup.version.version3_0", "lookup", "3.0", 0, "")
AddVersion("lookup.version.version4_0", "lookup", "4.0", 0, "")
AddVersionParent("lookup.version.version1", "lookup.version.version1")
AddVersionParent("lookup.version.version1", "vmodl.version.version0")
AddVersionParent("lookup.version.version1", "vmodl.version.version1")
AddVersionParent("lookup.version.version1", "vmodl.version.version2")
AddVersionParent("vmodl.version.version0", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version0")
AddVersionParent("vmodl.version.version1", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version0")
AddVersionParent("vmodl.version.version2", "vmodl.version.version1")
AddVersionParent("vmodl.version.version2", "vmodl.version.version2")
AddVersionParent("lookup.version.version1_5", "lookup.version.version1")
AddVersionParent("lookup.version.version1_5", "vmodl.version.version0")
AddVersionParent("lookup.version.version1_5", "vmodl.version.version1")
AddVersionParent("lookup.version.version1_5", "vmodl.version.version2")
AddVersionParent("lookup.version.version1_5", "lookup.version.version1_5")
AddVersionParent("lookup.version.version2", "lookup.version.version1")
AddVersionParent("lookup.version.version2", "vmodl.version.version0")
AddVersionParent("lookup.version.version2", "vmodl.version.version1")
AddVersionParent("lookup.version.version2", "vmodl.version.version2")
AddVersionParent("lookup.version.version2", "lookup.version.version1_5")
AddVersionParent("lookup.version.version2", "lookup.version.version2")
AddVersionParent("lookup.version.version3_0", "lookup.version.version1")
AddVersionParent("lookup.version.version3_0", "vmodl.version.version0")
AddVersionParent("lookup.version.version3_0", "vmodl.version.version1")
AddVersionParent("lookup.version.version3_0", "vmodl.version.version2")
AddVersionParent("lookup.version.version3_0", "lookup.version.version1_5")
AddVersionParent("lookup.version.version3_0", "lookup.version.version2")
AddVersionParent("lookup.version.version3_0", "lookup.version.version3_0")
AddVersionParent("lookup.version.version4_0", "lookup.version.version1")
AddVersionParent("lookup.version.version4_0", "vmodl.version.version0")
AddVersionParent("lookup.version.version4_0", "vmodl.version.version1")
AddVersionParent("lookup.version.version4_0", "vmodl.version.version2")
AddVersionParent("lookup.version.version4_0", "lookup.version.version1_5")
AddVersionParent("lookup.version.version4_0", "lookup.version.version2")
AddVersionParent("lookup.version.version4_0", "lookup.version.version3_0")
AddVersionParent("lookup.version.version4_0", "lookup.version.version4_0")

newestVersions.Add("lookup.version.version4_0")
stableVersions.Add("lookup.version.version4_0")
publicVersions.Add("lookup.version.version4_0")
dottedVersions.Add("lookup.version.version4_0")
oldestVersions.Add("lookup.version.version1")

CreateManagedType("lookup.DeploymentInformationService", "LookupDeploymentInformationService", "vmodl.ManagedObject", "lookup.version.version1", None, [("retrieveHaBackupConfiguration", "RetrieveHaBackupConfiguration", "lookup.version.version1", (), (0, "lookup.HaBackupNodeConfiguration", "lookup.HaBackupNodeConfiguration"), "LookupService.Administrator", None)])
CreateDataType("lookup.HaBackupNodeConfiguration", "LookupHaBackupNodeConfiguration", "vmodl.DynamicData", "lookup.version.version1", [("dbType", "string", "lookup.version.version1", 0), ("dbJdbcUrl", "string", "lookup.version.version1", 0), ("dbUser", "string", "lookup.version.version1", 0), ("dbPass", "string", "lookup.version.version1", F_SECRET)])
CreateManagedType("lookup.L10n", "LookupL10n", "vmodl.ManagedObject", "lookup.version.version1", [("defaultLocale", "string", "lookup.version.version1", 0, "System.Anonymous"), ("supportedLocales", "string[]", "lookup.version.version1", 0, "System.Anonymous")], [("setLocale", "SetLocale", "lookup.version.version1", (("locale", "string", "lookup.version.version1", 0, None),), (0, "string", "string"), "System.Anonymous", None), ("getLocale", "GetLocale", "lookup.version.version1", (), (0, "string", "string"), "System.Anonymous", None)])
CreateManagedType("lookup.LookupService", "LookupLookupService", "vmodl.ManagedObject", "lookup.version.version1", None, [("registerService", "RegisterService", "lookup.version.version1", (("registrationForm", "lookup.ServiceRegistrationForm", "lookup.version.version1", 0, None),), (0, "lookup.Service", "lookup.Service"), "LookupService.Administrator", ["lookup.fault.ServiceFault", "vmodl.fault.InvalidArgument", "vmodl.fault.SecurityError", ]), ("unregisterService", "UnregisterService", "lookup.version.version1", (("serviceId", "string", "lookup.version.version1", 0, None),), (0, "void", "void"), "LookupService.Owner", ["lookup.fault.UnsupportedSiteFault", "lookup.fault.EntryNotFoundFault", "lookup.fault.ServiceFault", "vmodl.fault.InvalidArgument", "vmodl.fault.SecurityError", ]), ("updateService", "UpdateService", "lookup.version.version1", (("service", "lookup.Service", "lookup.version.version1", 0, None),), (0, "void", "void"), "LookupService.Owner", ["lookup.fault.UnsupportedSiteFault", "lookup.fault.EntryNotFoundFault", "lookup.fault.ServiceFault", "vmodl.fault.InvalidArgument", "vmodl.fault.SecurityError", ]), ("find", "Find", "lookup.version.version1", (("searchCriteria", "lookup.SearchCriteria", "lookup.version.version1", 0, None),), (F_OPTIONAL, "lookup.Service[]", "lookup.Service[]"), "System.Anonymous", ["lookup.fault.ServiceFault", "vmodl.fault.InvalidArgument", "vmodl.fault.SecurityError", ]), ("findService", "FindService", "lookup.version.version1", (("serviceId", "string", "lookup.version.version1", 0, None),), (F_OPTIONAL, "lookup.Service", "lookup.Service"), "System.Anonymous", ["lookup.fault.ServiceFault", "vmodl.fault.InvalidArgument", "vmodl.fault.SecurityError", ]), ("getViSite", "GetViSite", "lookup.version.version1", (), (0, "string", "string"), "System.Anonymous", ["lookup.fault.ServiceFault", ])])
CreateDataType("lookup.SearchCriteria", "LookupSearchCriteria", "vmodl.DynamicData", "lookup.version.version1", [("serviceType", "vmodl.URI", "lookup.version.version1", F_OPTIONAL), ("viSite", "string", "lookup.version.version1", F_OPTIONAL), ("endpointProtocol", "string", "lookup.version.version1", F_OPTIONAL)])
CreateDataType("lookup.Service", "LookupService", "vmodl.DynamicData", "lookup.version.version1", [("serviceId", "string", "lookup.version.version1", 0), ("version", "string", "lookup.version.version1", 0), ("type", "vmodl.URI", "lookup.version.version1", 0), ("ownerId", "string", "lookup.version.version1", F_OPTIONAL), ("serviceName", "string", "lookup.version.version1", F_OPTIONAL), ("description", "string", "lookup.version.version1", F_OPTIONAL), ("endpoints", "lookup.ServiceEndpoint[]", "lookup.version.version1", 0), ("viSite", "string", "lookup.version.version1", 0), ("productId", "string", "lookup.version.version1", F_OPTIONAL)])
CreateDataType("lookup.ServiceContent", "LookupServiceContent", "vmodl.DynamicData", "lookup.version.version1", [("lookupService", "lookup.LookupService", "lookup.version.version1", 0), ("serviceRegistration", "lookup.ServiceRegistration", "lookup.version.version2", 0), ("deploymentInformationService", "lookup.DeploymentInformationService", "lookup.version.version1", 0), ("l10n", "lookup.L10n", "lookup.version.version1", 0)])
CreateDataType("lookup.ServiceEndpoint", "LookupServiceEndpoint", "vmodl.DynamicData", "lookup.version.version1", [("sslTrustAnchor", "string", "lookup.version.version1", F_OPTIONAL), ("url", "vmodl.URI", "lookup.version.version1", 0), ("protocol", "string", "lookup.version.version1", 0)])
CreateEnumType("lookup.ServiceEndpoint.EndpointProtocol", "LookupServiceEndpointEndpointProtocol", "lookup.version.version1", ["vmomi", "wsTrust", "rest", "http", "unknown"])
CreateManagedType("lookup.ServiceInstance", "LookupServiceInstance", "vmodl.ManagedObject", "lookup.version.version1", None, [("retrieveServiceContent", "RetrieveServiceContent", "lookup.version.version1", (), (0, "lookup.ServiceContent", "lookup.ServiceContent"), "System.Anonymous", None)])
CreateManagedType("lookup.ServiceRegistration", "LookupServiceRegistration", "vmodl.ManagedObject", "lookup.version.version2", None, [("create", "Create", "lookup.version.version2", (("serviceId", "string", "lookup.version.version2", 0, None),("createSpec", "lookup.ServiceRegistration.CreateSpec", "lookup.version.version2", 0, None),), (0, "void", "void"), "LookupService.Owner", ["lookup.fault.EntryExistsFault", "vmodl.fault.InvalidArgument", "vmodl.fault.SecurityError", ]), ("delete", "Delete", "lookup.version.version2", (("serviceId", "string", "lookup.version.version2", 0, None),), (0, "void", "void"), "LookupService.Owner", ["lookup.fault.EntryNotFoundFault", "vmodl.fault.SecurityError", ]), ("set", "Set", "lookup.version.version2", (("serviceId", "string", "lookup.version.version2", 0, None),("serviceSpec", "lookup.ServiceRegistration.SetSpec", "lookup.version.version2", 0, None),), (0, "void", "void"), "LookupService.Owner", ["lookup.fault.EntryNotFoundFault", "vmodl.fault.InvalidArgument", "vmodl.fault.SecurityError", ]), ("setTrustAnchor", "SetTrustAnchor", "lookup.version.version3_0", (("filter", "lookup.ServiceRegistration.Filter", "lookup.version.version3_0", 0, None),("trustAnchors", "string[]", "lookup.version.version3_0", 0, None),), (F_OPTIONAL, "int", "int"), "LookupService.Owner", ["vmodl.fault.InvalidArgument", "vmodl.fault.SecurityError", ]), ("get", "Get", "lookup.version.version2", (("serviceId", "string", "lookup.version.version2", 0, None),), (0, "lookup.ServiceRegistration.Info", "lookup.ServiceRegistration.Info"), "System.Anonymous", ["lookup.fault.EntryNotFoundFault", ]), ("list", "List", "lookup.version.version2", (("filterCriteria", "lookup.ServiceRegistration.Filter", "lookup.version.version2", F_OPTIONAL, None),), (F_OPTIONAL, "lookup.ServiceRegistration.Info[]", "lookup.ServiceRegistration.Info[]"), "System.Anonymous", None), ("getSiteId", "GetSiteId", "lookup.version.version2", (), (0, "string", "string"), "System.Anonymous", None)])
CreateDataType("lookup.ServiceRegistration.MutableServiceInfo", "LookupServiceRegistrationMutableServiceInfo", "vmodl.DynamicData", "lookup.version.version2", [("serviceVersion", "string", "lookup.version.version2", 0), ("vendorNameResourceKey", "string", "lookup.version.version2", F_OPTIONAL), ("vendorNameDefault", "string", "lookup.version.version2", F_OPTIONAL), ("vendorProductInfoResourceKey", "string", "lookup.version.version2", F_OPTIONAL), ("vendorProductInfoDefault", "string", "lookup.version.version2", F_OPTIONAL), ("serviceEndpoints", "lookup.ServiceRegistration.Endpoint[]", "lookup.version.version2", F_OPTIONAL), ("serviceAttributes", "lookup.ServiceRegistration.Attribute[]", "lookup.version.version2", F_OPTIONAL), ("serviceNameResourceKey", "string", "lookup.version.version2", F_OPTIONAL), ("serviceNameDefault", "string", "lookup.version.version2", F_OPTIONAL), ("serviceDescriptionResourceKey", "string", "lookup.version.version2", F_OPTIONAL), ("serviceDescriptionDefault", "string", "lookup.version.version2", F_OPTIONAL)])
CreateDataType("lookup.ServiceRegistration.CommonServiceInfo", "LookupServiceRegistrationCommonServiceInfo", "lookup.ServiceRegistration.MutableServiceInfo", "lookup.version.version2", [("ownerId", "string", "lookup.version.version2", 0), ("serviceType", "lookup.ServiceRegistration.ServiceType", "lookup.version.version2", 0), ("nodeId", "string", "lookup.version.version2", F_OPTIONAL)])
CreateDataType("lookup.ServiceRegistration.CreateSpec", "LookupServiceRegistrationCreateSpec", "lookup.ServiceRegistration.CommonServiceInfo", "lookup.version.version2", None)
CreateDataType("lookup.ServiceRegistration.SetSpec", "LookupServiceRegistrationSetSpec", "lookup.ServiceRegistration.MutableServiceInfo", "lookup.version.version2", None)
CreateDataType("lookup.ServiceRegistration.Info", "LookupServiceRegistrationInfo", "lookup.ServiceRegistration.CommonServiceInfo", "lookup.version.version2", [("serviceId", "string", "lookup.version.version2", 0), ("siteId", "string", "lookup.version.version2", 0)])
CreateDataType("lookup.ServiceRegistration.ServiceType", "LookupServiceRegistrationServiceType", "vmodl.DynamicData", "lookup.version.version2", [("product", "string", "lookup.version.version2", 0), ("type", "string", "lookup.version.version2", 0)])
CreateDataType("lookup.ServiceRegistration.Endpoint", "LookupServiceRegistrationEndpoint", "vmodl.DynamicData", "lookup.version.version2", [("url", "vmodl.URI", "lookup.version.version2", 0), ("endpointType", "lookup.ServiceRegistration.EndpointType", "lookup.version.version2", 0), ("sslTrust", "string[]", "lookup.version.version2", F_OPTIONAL), ("endpointAttributes", "lookup.ServiceRegistration.Attribute[]", "lookup.version.version2", F_OPTIONAL)])
CreateDataType("lookup.ServiceRegistration.EndpointType", "LookupServiceRegistrationEndpointType", "vmodl.DynamicData", "lookup.version.version2", [("protocol", "string", "lookup.version.version2", F_OPTIONAL), ("type", "string", "lookup.version.version2", F_OPTIONAL)])
CreateDataType("lookup.ServiceRegistration.Attribute", "LookupServiceRegistrationAttribute", "vmodl.DynamicData", "lookup.version.version2", [("key", "string", "lookup.version.version2", 0), ("value", "string", "lookup.version.version2", 0)])
CreateDataType("lookup.ServiceRegistration.Filter", "LookupServiceRegistrationFilter", "vmodl.DynamicData", "lookup.version.version2", [("siteId", "string", "lookup.version.version2", F_OPTIONAL), ("nodeId", "string", "lookup.version.version2", F_OPTIONAL), ("serviceType", "lookup.ServiceRegistration.ServiceType", "lookup.version.version2", F_OPTIONAL), ("endpointType", "lookup.ServiceRegistration.EndpointType", "lookup.version.version2", F_OPTIONAL), ("endpointTrustAnchor", "string", "lookup.version.version3_0", F_OPTIONAL), ("searchAllSsoDomains", "boolean", "lookup.version.version4_0", F_OPTIONAL)])
CreateDataType("lookup.ServiceRegistrationForm", "LookupServiceRegistrationForm", "vmodl.DynamicData", "lookup.version.version1", [("version", "string", "lookup.version.version1", 0), ("type", "vmodl.URI", "lookup.version.version1", 0), ("ownerId", "string", "lookup.version.version1", F_OPTIONAL), ("serviceName", "string", "lookup.version.version1", F_OPTIONAL), ("description", "string", "lookup.version.version1", F_OPTIONAL), ("endpoints", "lookup.ServiceEndpoint[]", "lookup.version.version1", 0), ("productId", "string", "lookup.version.version1", F_OPTIONAL), ("legacyId", "string", "lookup.version.version1_5", F_OPTIONAL)])
CreateDataType("lookup.fault.ServiceFault", "LookupFaultServiceFault", "vmodl.MethodFault", "lookup.version.version1", [("errorMessage", "string", "lookup.version.version1", F_OPTIONAL)])
CreateDataType("lookup.fault.UnsupportedSiteFault", "LookupFaultUnsupportedSiteFault", "lookup.fault.ServiceFault", "lookup.version.version1", [("operatingSite", "string", "lookup.version.version1", 0), ("requestedSite", "string", "lookup.version.version1", 0)])
CreateDataType("lookup.fault.EntryExistsFault", "LookupFaultEntryExistsFault", "lookup.fault.ServiceFault", "lookup.version.version2", [("name", "string", "lookup.version.version2", 0)])
CreateDataType("lookup.fault.EntryNotFoundFault", "LookupFaultEntryNotFoundFault", "lookup.fault.ServiceFault", "lookup.version.version1", [("name", "string", "lookup.version.version1", 0)])
