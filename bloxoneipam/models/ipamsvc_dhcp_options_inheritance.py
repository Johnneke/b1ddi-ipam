# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.     # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class IpamsvcDHCPOptionsInheritance(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'dhcp_options': 'IpamsvcInheritedDHCPOptionList'
    }

    attribute_map = {
        'dhcp_options': 'dhcp_options'
    }

    def __init__(self, dhcp_options=None):  # noqa: E501
        """IpamsvcDHCPOptionsInheritance - a model defined in Swagger"""  # noqa: E501

        self._dhcp_options = None
        self.discriminator = None

        if dhcp_options is not None:
            self.dhcp_options = dhcp_options

    @property
    def dhcp_options(self):
        """Gets the dhcp_options of this IpamsvcDHCPOptionsInheritance.  # noqa: E501

        Optional. Field config for dhcp_options field.  # noqa: E501

        :return: The dhcp_options of this IpamsvcDHCPOptionsInheritance.  # noqa: E501
        :rtype: IpamsvcInheritedDHCPOptionList
        """
        return self._dhcp_options

    @dhcp_options.setter
    def dhcp_options(self, dhcp_options):
        """Sets the dhcp_options of this IpamsvcDHCPOptionsInheritance.

        Optional. Field config for dhcp_options field.  # noqa: E501

        :param dhcp_options: The dhcp_options of this IpamsvcDHCPOptionsInheritance.  # noqa: E501
        :type: IpamsvcInheritedDHCPOptionList
        """

        self._dhcp_options = dhcp_options

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IpamsvcDHCPOptionsInheritance, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IpamsvcDHCPOptionsInheritance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
