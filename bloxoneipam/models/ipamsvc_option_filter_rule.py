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


class IpamsvcOptionFilterRule(object):
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
        'compare': 'str',
        'option_code': 'str',
        'option_value': 'str',
        'substring_offset': 'int'
    }

    attribute_map = {
        'compare': 'compare',
        'option_code': 'option_code',
        'option_value': 'option_value',
        'substring_offset': 'substring_offset'
    }

    def __init__(self, compare=None, option_code=None, option_value=None, substring_offset=None):  # noqa: E501
        """IpamsvcOptionFilterRule - a model defined in Swagger"""  # noqa: E501

        self._compare = None
        self._option_code = None
        self._option_value = None
        self._substring_offset = None
        self.discriminator = None

        self.compare = compare
        self.option_code = option_code
        if option_value is not None:
            self.option_value = option_value
        if substring_offset is not None:
            self.substring_offset = substring_offset

    @property
    def compare(self):
        """Gets the compare of this IpamsvcOptionFilterRule.  # noqa: E501

        How to compare the option_value to the client option.  Success by comparison: - equals: value and client option are the same - not_equals: value and client option are not the same - exists: client option exists - not_exists: client option does not exist - substring: value is the specified substring of the option - not_substring: value is not the specified substring of the option  # noqa: E501

        :return: The compare of this IpamsvcOptionFilterRule.  # noqa: E501
        :rtype: str
        """
        return self._compare

    @compare.setter
    def compare(self, compare):
        """Sets the compare of this IpamsvcOptionFilterRule.

        How to compare the option_value to the client option.  Success by comparison: - equals: value and client option are the same - not_equals: value and client option are not the same - exists: client option exists - not_exists: client option does not exist - substring: value is the specified substring of the option - not_substring: value is not the specified substring of the option  # noqa: E501

        :param compare: The compare of this IpamsvcOptionFilterRule.  # noqa: E501
        :type: str
        """
        if compare is None:
            raise ValueError("Invalid value for `compare`, must not be `None`")  # noqa: E501

        self._compare = compare

    @property
    def option_code(self):
        """Gets the option_code of this IpamsvcOptionFilterRule.  # noqa: E501

        The resource identifier.  # noqa: E501

        :return: The option_code of this IpamsvcOptionFilterRule.  # noqa: E501
        :rtype: str
        """
        return self._option_code

    @option_code.setter
    def option_code(self, option_code):
        """Sets the option_code of this IpamsvcOptionFilterRule.

        The resource identifier.  # noqa: E501

        :param option_code: The option_code of this IpamsvcOptionFilterRule.  # noqa: E501
        :type: str
        """
        if option_code is None:
            raise ValueError("Invalid value for `option_code`, must not be `None`")  # noqa: E501

        self._option_code = option_code

    @property
    def option_value(self):
        """Gets the option_value of this IpamsvcOptionFilterRule.  # noqa: E501

        Value to match against.  # noqa: E501

        :return: The option_value of this IpamsvcOptionFilterRule.  # noqa: E501
        :rtype: str
        """
        return self._option_value

    @option_value.setter
    def option_value(self, option_value):
        """Sets the option_value of this IpamsvcOptionFilterRule.

        Value to match against.  # noqa: E501

        :param option_value: The option_value of this IpamsvcOptionFilterRule.  # noqa: E501
        :type: str
        """

        self._option_value = option_value

    @property
    def substring_offset(self):
        """Gets the substring_offset of this IpamsvcOptionFilterRule.  # noqa: E501

        Offset where substring match starts, used only if compare is one of the substring modes.  # noqa: E501

        :return: The substring_offset of this IpamsvcOptionFilterRule.  # noqa: E501
        :rtype: int
        """
        return self._substring_offset

    @substring_offset.setter
    def substring_offset(self, substring_offset):
        """Sets the substring_offset of this IpamsvcOptionFilterRule.

        Offset where substring match starts, used only if compare is one of the substring modes.  # noqa: E501

        :param substring_offset: The substring_offset of this IpamsvcOptionFilterRule.  # noqa: E501
        :type: int
        """

        self._substring_offset = substring_offset

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
        if issubclass(IpamsvcOptionFilterRule, dict):
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
        if not isinstance(other, IpamsvcOptionFilterRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
