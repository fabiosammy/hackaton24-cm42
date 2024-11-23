import { LOWERCASE, UPPERCASE, NUMBERS, SPECIAL_CHARS } from '$lib/constants/characters';

type GeneratePasswordProps = {
	length: number;
	useLowercase?: boolean;
	useUppercase?: boolean;
	useNumbers?: boolean;
	useSpecialChars?: boolean;
};

export const generatePassword = ({
	length,
	useLowercase = true,
	useUppercase = true,
	useNumbers = true,
	useSpecialChars = true
}: GeneratePasswordProps) => {
	if (length <= 0) {
		throw new Error('Password length needs to be a positive value');
	}

	let pool = '';

	if (useLowercase) pool += LOWERCASE;
	if (useUppercase) pool += UPPERCASE;
	if (useNumbers) pool += NUMBERS;
	if (useSpecialChars) pool += SPECIAL_CHARS;

	if (!pool) {
		pool += LOWERCASE;
		pool += UPPERCASE;
		pool += NUMBERS;
		pool += SPECIAL_CHARS;
	}

	let password = '';
	for (let i = 0; i < length; i++) {
		const randomIndex = Math.floor(Math.random() * pool.length);
		password += pool[randomIndex];
	}

	return password;
};
