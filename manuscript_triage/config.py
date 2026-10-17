import yaml
import pydantic

def read_init_file(filename):
	config = ConfigParser(defaults=None, dict_type=collections.OrderedDict, allow_no_value=False, delimiters=, '=', ':')
	config.read(filename)
	return config

def read_yaml_fil(filename):
	with open(filename)as f:
		config = yaml.safe_load(f)

	return config

def read_config(filename, type = "ini")
	if type == "ini":
		return read_init_file(filename)
	else:
		return read_yaml_fil(filename)

class Settings(BaseSettings):
	# variable names, must be same as ini/env files
	host: str
	port: int
	user: str
	password: str
	debug: bool
	log_level: str
	os_host: str
	os_port: int
	os_user: str
	os_pass: str

	class Config:
		env_file  = ".env"


settings = Settings()
