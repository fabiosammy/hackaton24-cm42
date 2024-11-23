export type Vault = {
	id: string;
};

export type CredentialDTO = {
	id: string;
	name: string;
	username: string;
	password: string;
	otp_key?: string;
	description?: string;
	vault_id: string;
};

export type AppCredential = {
	id: string;
	name: string;
	username: string;
	password: string;
	otp_key?: string;
	description?: string;
	vault_id: string;
};
