"""
Meraki API Test script
"""
import json
from meraki_api import MerakiAPI

KEY = "76268186c0b0da0eb10af1ba92419703930f9322"
SERIAL = "Q2JD-XK95-Y9D5"
ORGANIZATION_ID = "405942"
NETWORK_ID = "N_579838452023959422"
ADMIN_ID = "123"
CONFIG_TEMPLATE = "1234"
SSID_NUM = "1234"
PHONE_CONTACTS_ID = "1234"
SAML_ROLE_ID = "1234"
STATIC_ROUTE_ID = "1234"
SWITCH_PORT_ID = "1234"
VLAN_ID = "1234"

if __name__ == "__main__":

    def puts(text):
        """ Prints a text after JSON stringifying it """
        print(json.dumps(text, indent=2))

    '''
    # Crear un usuario de administrador en la organización ORGANIZATION_ID
    print("\nCreating a new organization user")
    ADMIN = (
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins()
        .create({
            "email": "g_monne@yahoo.com",
            "name": "Guzman Monne",
            "orgAccess": "none",
            "tags": [{
                "tag": "preventa",
                "access": "read-only"
            }]
        })
    )
    puts(ADMIN.json())
    # Elimina el administrador creado en la organización.
    print("Deleting user", ADMIN.json()["id"])
    RESPONSE = (
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins(ADMIN.json()["id"])
        .delete()
    )
    print('Admin created and deleted.')
    # Trae todos los cliente registrados en un determinado equipos en los
    # ultimos `timespan` milisegundos.
    print("\nGet clients connected to the device.", SERIAL)
    puts(
        MerakiAPI(KEY)
        .devices(SERIAL)
        .clients({"timespan": 86400})
        .json()
    )
    # Trae todas las redes dentro de una organization.
    print("\nGet all the networks inside organization", ORGANIZATION_ID)
    puts(
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks()
        .index()
        .json()
    )
    # Trae detalles de una network.
    print("\nGet the details of network", NETWORK_ID)
    puts(
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .show()
        .json()
    )
    print("\nUpdate network", NETWORK_ID)
    # Actualiza una network.
    puts(
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .update({
            "tags": "tag_desde_api"
        })
        .json()
    )
    # Crea una nueva network dentro de una organization.
    print("\nCreated a new network inside organization", ORGANIZATION_ID)
    JSON = (
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks()
        .create({
            "name": "Red creada por la API",
            "type": "wireless",
            "tags": "tag_desde_api otra_tag",
            "timeZone": "America/Montevideo"
        })
        .json()
    )
    puts(JSON)
    # Elimina una network.
    (
        MerakiAPI(KEY)
        .networks(JSON["id"])
        .delete()
    )
    print('Network created and deleted.')
    # Traer todos los clientes detectados en un dispositivo.
    print("\nAll detected clients on device", SERIAL)
    puts(
        MerakiAPI(KEY)
        .devices(SERIAL)
        .clients({"timespan": 86400})
        .json()
    )
    # Trae el tráfico de analisis en una red.
    print("\nGets the traffic analisis from the second network.")
    NETWORK_ID = (
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks()
        .index()
        .json()
    )[1]["id"]
    puts(
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .traffic({
            "timespan": 7200,
            "deviceType": "wireless"
        })
        .json()
    )
    '''

    def equals(test, expected, actual):
        """ Test function to check to values. """
        print(str(test), end=" ...")
        try:
            if expected != actual:
                raise ValueError()
            print("OK!")
            return 0
        except ValueError:
            print(
                "Error: 'expected' does not equals 'actual'"
                , "\n"
                , str(expected)
                , "!="
                , str(actual)
            )
            return 1
        except Exception as error:
            print(str("Something unexpected happened:"), error + "\n")

    ERRORS = 0

    # Organizations.

    ERRORS += equals(
        "organizations.index",
        "https://dashboard.meraki.com/api/v0/organizations",
        MerakiAPI(KEY).organizations().lazy().index().cached.url
    )

    ERRORS += equals(
        "organizations.show",
        "https://dashboard.meraki.com/api/v0/organizations/" + ORGANIZATION_ID,
        MerakiAPI(KEY).organizations(ORGANIZATION_ID).lazy().show().cached.url
    )

    ORGANIZATION_DATA = {
        "name": "Organization name"
    }

    ERRORS += equals(
        "organizations.create",
        "https://dashboard.meraki.com/api/v0/organizations",
        MerakiAPI(KEY)
        .organizations()
        .lazy()
        .create(ORGANIZATION_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.update",
        "https://dashboard.meraki.com/api/v0/organizations/" + ORGANIZATION_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .update(ORGANIZATION_DATA)
        .cached.url
    )

    ERRORS += equals(
        "organizations.delete",
        "https://dashboard.meraki.com/api/v0/organizations/" + ORGANIZATION_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .delete()
        .cached.url
    )

    ERRORS += equals(
        "organizations.clone",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/clone",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .clone(ORGANIZATION_DATA)
        .cached.url
    )

    ERRORS += equals(
        "organizations.claim",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/clone",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .clone(ORGANIZATION_DATA)
        .cached.url
    )

    ERRORS += equals(
        "organizations.licenseState",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/licenseState",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .license_state()
        .cached.url
    )

    ERRORS += equals(
        "organizations.inventory",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/inventory",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .inventory()
        .cached.url
    )

    ERRORS += equals(
        "organizations.snmp",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/snmp",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .snmp()
        .cached.url
    )

    ERRORS += equals(
        "organizations.thirdPartyVPNPeers",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/thirdPartyVPNPeers",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .third_party_vpn_peers()
        .cached.url
    )

    THIRD_PARTY_VPN_DATA = [{
        "name": "Your peer",
        "publicIp": "192.168.0.1",
        "privateSubnets": [
            "172.168.0.0/16",
            "172.169.0.0/16"
        ],
        "secret": "asdf1234"
    }]

    ERRORS += equals(
        "organizations.updateThirdPartyVPNPeers",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/thirdPartyVPNPeers",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .lazy()
        .update_third_party_vpn_peers(THIRD_PARTY_VPN_DATA)
        .cached.url
    )

    # Organizations admins.

    ADMIN_DATA = {
        "email": "g_monne@yahoo.com",
        "name": "Guzman Monne",
        "orgAccess": "none",
        "tags": [{
            "tag": "preventa",
            "access": "read-only"
        }]
    }

    ERRORS += equals(
        "organizations.admins.index",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/admins",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins()
        .lazy()
        .index()
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.admins.show",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/admins/" + ADMIN_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins(ADMIN_ID)
        .lazy()
        .show()
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.admins.create",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/admins",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins()
        .lazy()
        .create(ADMIN_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.admins.delete",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/admins/"
        + ADMIN_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins(ADMIN_ID)
        .lazy()
        .delete()
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.admins.update",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID +
        "/admins/" +
        ADMIN_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .admins(ADMIN_ID).lazy()
        .update(ADMIN_DATA)
        .cached
        .url
    )

    # Organizations SAML roles.

    ERRORS += equals(
        "organizations.samlRoles.index",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID +
        "/samlRoles",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .saml_roles()
        .lazy()
        .index()
        .cached
        .url
    )

    SAML_ROLE_DATA = {
        "role": "myrole",
        "orgAccess": "none",
        "networks": [{
            "id": "N_1234",
            "access": "full"
        }],
        "tags": [{
            "tag": "west",
            "access": "read-only"
        }]
    }

    ERRORS += equals(
        "organizations.samlRoles.create",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/samlRoles",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .saml_roles()
        .lazy()
        .create(SAML_ROLE_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.samlRoles.show",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/samlRoles/"
        + SAML_ROLE_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .saml_roles(SAML_ROLE_ID)
        .lazy()
        .show()
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.samlRoles.update",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/samlRoles/"
        + SAML_ROLE_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .saml_roles(SAML_ROLE_ID)
        .lazy()
        .update(SAML_ROLE_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.samlRoles.delete",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/samlRoles/"
        + SAML_ROLE_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .saml_roles(SAML_ROLE_ID)
        .lazy()
        .delete()
        .cached
        .url
    )

    # Organizations networks.

    ERRORS += equals(
        "organizations.networks.index",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID +
        "/networks",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks()
        .lazy()
        .index()
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.networks.show",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/networks/"
        + NETWORK_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks(NETWORK_ID)
        .lazy()
        .show()
        .cached
        .url
    )

    NETWORK_DATA = {
        "name": "Red creada por la API",
        "type": "wireless",
        "tags": "tag_desde_api otra_tag",
        "timeZone": "America/Montevideo"
    }

    ERRORS += equals(
        "organizations.networks.create",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/networks",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks()
        .lazy()
        .create(NETWORK_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.networks.update",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/networks/"
        + NETWORK_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks(NETWORK_ID)
        .lazy()
        .update(NETWORK_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.networks.delete",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/networks/"
        + NETWORK_ID,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks(NETWORK_ID)
        .lazy()
        .delete()
        .cached
        .url
    )

    TRAFFIC_DATA = {
        "timespan": 7200,
        "deviceType": "wireless"
    }

    ERRORS += equals(
        "organizations.networks.traffic",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/networks/"
        + NETWORK_ID
        + "/traffic?timespan=7200&deviceType=wireless",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .networks(NETWORK_ID)
        .lazy()
        .traffic(TRAFFIC_DATA)
        .cached
        .url
    )

    # Organizations config templates.

    ERRORS += equals(
        "organizations.config_templates.index",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/configTemplates",
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .config_templates()
        .lazy()
        .index()
        .cached
        .url
    )

    ERRORS += equals(
        "organizations.config_templates.delete",
        "https://dashboard.meraki.com/api/v0/organizations/"
        + ORGANIZATION_ID
        + "/configTemplates/"
        + CONFIG_TEMPLATE,
        MerakiAPI(KEY)
        .organizations(ORGANIZATION_ID)
        .config_templates(CONFIG_TEMPLATE)
        .lazy()
        .delete()
        .cached
        .url
    )

    # Networks.

    ERRORS += equals(
        "networks.index",
        "https://dashboard.meraki.com/api/v0/networks",
        MerakiAPI(KEY).networks().lazy().index().cached.url
    )

    ERRORS += equals(
        "networks.show",
        "https://dashboard.meraki.com/api/v0/networks/" + NETWORK_ID,
        MerakiAPI(KEY).networks(NETWORK_ID).lazy().show().cached.url
    )

    NETWORK_DATA = {
        "name": "Red creada por la API",
        "type": "wireless",
        "tags": "tag_desde_api otra_tag",
        "timeZone": "America/Montevideo"
    }

    ERRORS += equals(
        "networks.create",
        "https://dashboard.meraki.com/api/v0/networks",
        MerakiAPI(KEY).networks().lazy().create(NETWORK_DATA).cached.url
    )

    ERRORS += equals(
        "networks.update",
        "https://dashboard.meraki.com/api/v0/networks/" + NETWORK_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .update(NETWORK_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "networks.delete",
        "https://dashboard.meraki.com/api/v0/networks/" + NETWORK_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .delete()
        .cached
        .url
    )

    TRAFFIC_DATA = {
        "timespan": 7200,
        "deviceType": "wireless"
    }

    ERRORS += equals(
        "networks.traffic",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/traffic?timespan=7200&deviceType=wireless",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .traffic(TRAFFIC_DATA)
        .cached
        .url
    )

    BIND_DATA = {
        "configTemplateId":"{{templateId}}",
        "autoBind": False
    }

    ERRORS += equals(
        "networks.bind",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/bind",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .bind(TRAFFIC_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "networks.unbind",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/unbind",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .unbind()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.accessPolicies",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/accessPolicies",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .access_policies()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.airMarshal",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/airMarshal?timespan=7200",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .air_marshal({"timespan": 7200})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.phoneNumbers",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/phoneNumbers",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .phone_numbers()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.phoneNumbers.available",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/phoneNumbers/available",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .lazy()
        .available_phone_numbers()
        .cached
        .url
    )

    # Network phone contacts.

    ERRORS += equals(
        "networks.phoneContacts.index",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/phoneContacts",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .phone_contacts()
        .lazy()
        .index()
        .cached
        .url
    )

    PHONE_CONTACTS_DATA = {"name": "Phone Contact Name"}

    ERRORS += equals(
        "networks.phoneContacts.create",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/phoneContacts",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .phone_contacts()
        .lazy()
        .create(PHONE_CONTACTS_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "networks.phoneContacts.show",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/phoneContacts/"
        + PHONE_CONTACTS_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .phone_contacts(PHONE_CONTACTS_ID)
        .lazy()
        .show()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.phoneContacts.update",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/phoneContacts/"
        + PHONE_CONTACTS_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .phone_contacts(PHONE_CONTACTS_ID)
        .lazy()
        .update(PHONE_CONTACTS_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "networks.phoneContacts.delete",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/phoneContacts/"
        + PHONE_CONTACTS_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .phone_contacts(PHONE_CONTACTS_ID)
        .lazy()
        .delete()
        .cached
        .url
    )

    # Network site-to-site-vpn.

    ERRORS += equals(
        "networks.siteToSiteVpn.index",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/siteToSiteVpn",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .site_to_site_vpn()
        .lazy()
        .index()
        .cached
        .url
    )

    SITE_TO_SITE_VPN_DATA = {
        "mode": "spoke",
        "hubs":[{
            "hubId": "N_1234",
            "useDefaultRoute": True
        }, {
            "hubId": "N_2345",
            "useDefaultRoute": False
        }],
        "subnets":[{
            "localSubnet": "192.168.1.0/24",
            "useVpn": True
        }, {
            "localSubnet": "192.168.128.0/24",
            "useVpn": True
        }]
    }

    ERRORS += equals(
        "networks.siteToSiteVpn.update",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/siteToSiteVpn",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .site_to_site_vpn()
        .lazy()
        .update(SITE_TO_SITE_VPN_DATA)
        .cached
        .url
    )

    # Network devices.

    ERRORS += equals(
        "networks.devices.index",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/devices",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .devices()
        .lazy()
        .index()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.devices.show",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/devices/"
        + SERIAL,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .devices(SERIAL)
        .lazy()
        .show()
        .cached
        .url
    )

    DEVICE_DATA = {
        "name":"Your AP",
        "tags":" recently-added ",
        "lat": 37.4180951010362,
        "lng": -122.098531723022,
        "address":"1600 Pennsylvania Ave",
        "moveMapMarker": True
    }

    ERRORS += equals(
        "networks.devices.update",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/devices/"
        + SERIAL,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .devices(SERIAL)
        .lazy()
        .update(DEVICE_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "networks.devices.uplink",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/devices/"
        + SERIAL
        + "/uplink",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .devices(SERIAL)
        .lazy()
        .uplink()
        .cached
        .url
    )

    CLAIM_DATA = {
        "serial": "Q2XX-XXXX-XXXX"
    }

    ERRORS += equals(
        "networks.devices.claim",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/devices/claim",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .devices()
        .lazy()
        .claim(CLAIM_DATA)
        .cached
        .url
    )

    ERRORS += equals(
        "networks.devices.remove",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/devices/"
        + SERIAL
        + "/remove",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .devices(SERIAL)
        .lazy()
        .remove()
        .cached
        .url
    )

    # Network VLANs

    ERRORS += equals(
        "networks.vlans.index",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/vlans",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .vlans()
        .lazy()
        .index()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.vlans.create",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/vlans",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .vlans()
        .lazy()
        .create({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.vlans.show",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/vlans/"
        + VLAN_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .vlans(VLAN_ID)
        .lazy()
        .show()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.vlans.update",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/vlans/"
        + VLAN_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .vlans(VLAN_ID)
        .lazy()
        .update({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.vlans.delete",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/vlans/"
        + VLAN_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .vlans(VLAN_ID)
        .lazy()
        .delete()
        .cached
        .url
    )

    # Network Static Routes

    ERRORS += equals(
        "networks.staticRoutes.index",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/staticRoutes",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .static_routes()
        .lazy()
        .index()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.staticRoutes.create",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/staticRoutes",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .static_routes()
        .lazy()
        .create({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.staticRoutes.show",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/staticRoutes/"
        + STATIC_ROUTE_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .static_routes(STATIC_ROUTE_ID)
        .lazy()
        .show()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.staticRoutes.update",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/staticRoutes/"
        + STATIC_ROUTE_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .static_routes(STATIC_ROUTE_ID)
        .lazy()
        .update({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.staticRoutes.delete",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/staticRoutes/"
        + STATIC_ROUTE_ID,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .static_routes(STATIC_ROUTE_ID)
        .lazy()
        .delete()
        .cached
        .url
    )

    # Network SSIDs

    ERRORS += equals(
        "networks.ssids.index",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/ssids",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .ssids()
        .lazy()
        .index()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.ssids.show",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/ssids/"
        + SSID_NUM,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .ssids(SSID_NUM)
        .lazy()
        .show()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.ssids.update",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/ssids/"
        + SSID_NUM,
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .ssids(SSID_NUM)
        .lazy()
        .update({})
        .cached
        .url
    )

    # Network SSIDs L3 Firewall Rules

    ERRORS += equals(
        "networks.ssids.l3_firewall_rules.index",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/ssids/"
        + SSID_NUM
        + "/l3FirewallRules",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .ssids(SSID_NUM)
        .l3_firewall_rules()
        .lazy()
        .index()
        .cached
        .url
    )

    L3_FIREWALL_RULE_DATA = {
        "rules": [{
            "comment": "a note about the rule",
            "policy": "deny",
            "protocol": "tcp",
            "destPort": "any",
            "destCidr": "192.168.1.0/24"
        }],
        "allowLanAccess": True
    }

    ERRORS += equals(
        "networks.ssids.l3_firewall_rules.update",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/ssids/"
        + SSID_NUM
        + "/l3FirewallRules",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .ssids(SSID_NUM)
        .l3_firewall_rules()
        .lazy()
        .update(L3_FIREWALL_RULE_DATA)
        .cached
        .url
    )

    # Network SM

    ERRORS += equals(
        "networks.sm.devices",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/sm/devices",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .sm()
        .lazy()
        .devices()
        .cached
        .url
    )

    ERRORS += equals(
        "networks.sm.modify_devices_tags",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/sm/devices/tags",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .sm()
        .lazy()
        .modify_devices_tags({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.sm.modify_device_fields",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/sm/device/fields",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .sm()
        .lazy()
        .modify_device_fields({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.sm.lock_devices",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/sm/devices/lock",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .sm()
        .lazy()
        .lock_devices({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.sm.wipe_devices",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/sm/device/wipe",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .sm()
        .lazy()
        .wipe_device({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.sm.wipe_devices",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/sm/devices/checkin",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .sm()
        .lazy()
        .check_in({})
        .cached
        .url
    )

    ERRORS += equals(
        "networks.sm.move",
        "https://dashboard.meraki.com/api/v0/networks/"
        + NETWORK_ID
        + "/sm/devices/move",
        MerakiAPI(KEY)
        .networks(NETWORK_ID)
        .sm()
        .lazy()
        .move_devices({})
        .cached
        .url
    )

    # Devices switch ports

    ERRORS += equals(
        "devices.switchPorts.index",
        "https://dashboard.meraki.com/api/v0/devices/"
        + SERIAL
        + "/switchPorts",
        MerakiAPI(KEY)
        .devices(SERIAL)
        .switch_ports()
        .lazy()
        .index()
        .cached
        .url
    )

    ERRORS += equals(
        "devices.switchPorts.create",
        "https://dashboard.meraki.com/api/v0/devices/"
        + SERIAL
        + "/switchPorts",
        MerakiAPI(KEY)
        .devices(SERIAL)
        .switch_ports()
        .lazy()
        .create({})
        .cached
        .url
    )

    ERRORS += equals(
        "devices.switchPorts.index",
        "https://dashboard.meraki.com/api/v0/devices/"
        + SERIAL
        + "/switchPorts/"
        + SWITCH_PORT_ID,
        MerakiAPI(KEY)
        .devices(SERIAL)
        .switch_ports(SWITCH_PORT_ID)
        .lazy()
        .show()
        .cached
        .url
    )

    ERRORS += equals(
        "devices.switchPorts.update",
        "https://dashboard.meraki.com/api/v0/devices/"
        + SERIAL
        + "/switchPorts/"
        + SWITCH_PORT_ID,
        MerakiAPI(KEY)
        .devices(SERIAL)
        .switch_ports(SWITCH_PORT_ID)
        .lazy()
        .update({})
        .cached
        .url
    )

    ERRORS += equals(
        "devices.switchPorts.delete",
        "https://dashboard.meraki.com/api/v0/devices/"
        + SERIAL
        + "/switchPorts/"
        + SWITCH_PORT_ID,
        MerakiAPI(KEY)
        .devices(SERIAL)
        .switch_ports(SWITCH_PORT_ID)
        .lazy()
        .delete()
        .cached
        .url
    )


    def pluralize(singular, plural, count):
        """ returns the singular or plural form according to the count. """
        if count > 1:
            return plural
        else:
            return singular

    if ERRORS == 0:
        print("\nNo se han encontrado errores.")
    else:
        print(
            "\nSe"
            , pluralize("ha", "han", ERRORS)
            , "encontrado"
            , pluralize("erorres", "error", ERRORS)
        )
