export type Vault = {
	id: string;
	name: string;
};

export type CredentialDTO = {
	id: string;
	name: string;
	username: string;
	password: string;
	otp_key?: string;
	description?: string;
	tags: string[];
	vault_id: string;
};

export type AppCredential = {
	name: string;
	username: string;
	description?: string;
	password: string;
};
