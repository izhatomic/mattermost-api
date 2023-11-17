from typing import Union, List, Dict
from Mattermost_Base import Base


class saml(Base):
    def __init__(self, token: str, server_url: str):
        super().__init__(token, server_url)
        self.api_url = f"{self.base_url}/saml"


    def migrate_user_acc_auth_type_to_saml(self, from:str, matches: dict, auto: bool) -> dict:
        """
        Migrates accounts from one authentication provider to another.
        For example, you can upgrade your authentication provider from email to SAML.
        Minimum server version: 5.28
        Must have manage_system permission.
        :param from: The current authentication type for the matched users.
        :param matches: Users map.
        :param auto: Toggle auto migration.
        :return: User account migration info.
        """
        url = f"{self.base_url}/users/migrate_auth/saml"
        self.reset()
        self.add_application_json_header()
        if from is not None:
            self.add_to_json('from', from)
        if matches is not None:
            self.add_to_json('matches', matches)
        if auto is not None:
            self.add_to_json('auto', auto)

        return self.request(url, request_type='POST', body=True)

    def get_metadata(self) -> dict:
        """
        Get SAML metadata from the server. SAML must be configured properly.
        No permission required.
        :return: SAML retrieval info.
        """
        url = f"{self.api_url}/metadata"
        self.reset()

        return self.request(url, request_type='GET')

    def get_metadata_from_identity_provider(self, saml_metadata_url: str) -> dict:
        """
        Get SAML metadata from the Identity Provider. SAML must be configured properly.
        No permission required.
        :param saml_metadata_url: The URL from which to retrieve the SAML IDP data.
        :return: SAML retrieval info.
        """
        url = f"{self.api_url}/metadatafromidp"
        self.reset()
        self.add_application_json_header()
        if from is not None:
            self.add_to_json('saml_metadata_url', saml_metadata_url)

        return self.request(url, request_type='POST')

    def upload_idp_certificate(self, certificate: str) -> dict:
        """
        Upload the IDP certificate to be used with your SAML configuration.
        The server will pick a hard-coded filename for the IdpCertificateFile setting in your config.json.
        Must have sysconsole_write_authentication permission.
        :param certificate: The  IDP certificate file
        :return: SAML certificate info.
        """
        url = f"{self.api_url}/certificate/idp"
        self.reset()
        self.add_application_json_header()
        if certificate is not None:
            self.add_to_json('certificate', certificate)

        return self.request(url, request_type='POST', body=True)

    def remove_idp_certificate(self) -> dict:
        """
        Delete the current IDP certificate being used with your SAML configuration.
        This will also disable SAML on your system as this certificate is required for SAML.
        Must have sysconsole_write_authentication permission.
        :return: SAML certificate info.
        """
        url = f"{self.api_url}/certificate/idp"
        self.reset()

        return self.request(url, request_type='DEL')

    def upload_public_certificate(self, certificate: str) -> dict:
        """
        Upload the public certificate to be used for encryption with your SAML configuration. The server will pick a hard-coded filename for the PublicCertificateFile setting in your config.json.
        Must have sysconsole_write_authentication permission.
        :param certificate: The public certificate file
        :return: SAML certificate info.
        """
        url = f"{self.api_url}/certificate/public"
        self.reset()
        self.add_application_json_header()
        if certificate is not None:
            self.add_to_json('certificate', certificate)

        return self.request(url, request_type='POST', body=True)

    def remove_public_certificate(self) -> dict:
        """
        Delete the current public certificate being used with your SAML configuration.
        This will also disable encryption for SAML on your system as this certificate is required for that.
        Must have sysconsole_write_authentication permission.
        :return: SAML certificate info.
        """
        url = f"{self.api_url}/certificate/public"
        self.reset()

        return self.request(url, request_type='DEL')

    def upload_private_key(self, certificate: str) -> dict:
        """
        Upload the private key to be used for encryption with your SAML configuration. The server will pick a hard-coded filename for the PrivateKeyFile setting in your config.json.
        Must have sysconsole_write_authentication permission.
        :param certificate: The private key file
        :return: SAML certificate info.
        """
        url = f"{self.api_url}/certificate/private"
        self.reset()
        self.add_application_json_header()
        if certificate is not None:
            self.add_to_json('certificate', certificate)

        return self.request(url, request_type='POST', body=True)

    def remove_private_key(self) -> dict:
        """
        Delete the current private key being used with your SAML configuration.
        This will also disable encryption for SAML on your system as this key is required for that.
        Must have sysconsole_write_authentication permission.
        :return: SAML certificate info.
        """
        url = f"{self.api_url}/certificate/private"
        self.reset()

        return self.request(url, request_type='DEL')

    def get_certificate_status(self) -> dict:
        """
        Get the status of the uploaded certificates and keys in use by your SAML configuration.
        Must have sysconsole_write_authentication permission.
        Minimum server version: 5.35
        :return: SAML certificate info.
        """
        url = f"{self.api_url}/certificate/status"
        self.reset()

        return self.request(url, request_type='GET')

    def reset_authdata_to_email(self,
                                include_deleted: bool,
                                dry_run: bool,
                                user_ids: list[str]) -> dict:
        """
        Reset the AuthData field of SAML users to their email.
        This is meant to be used when the "id" attribute is set to an empty value ("")
        from a previously non-empty value.
        Must have manage_system permission.
        Minimum server version: 5.35
        :param include_deleted: Default: false. Whether to include deleted users.
        :param dry_run: Default: false. If set to true, the number of users who would be affected is returned.
        :param user_ids: Default: []. If set to a non-empty array, then users whose IDs are not in the array will be excluded.
        :return: LDAP certificate info.
        """
        url = f"{self.api_url}/certificate/private"
        self.reset()
        self.add_application_json_header()
        if include_deleted is not None:
            self.add_to_json('include_deleted', include_deleted)
        if dry_run is not None:
            self.add_to_json('dry_run', dry_run)
        if user_ids is not None:
            self.add_to_json('user_ids', user_ids)

        return self.request(url, request_type='POST', body=True)
