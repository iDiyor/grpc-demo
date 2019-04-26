package config

import (
	"encoding/json"
	"errors"
	"io/ioutil"
)

var (
	errInvalidConfigPath = errors.New("Invalid config path")
)

// Config ...
type Config struct {
	RPCPort string
}

// Load ...
func Load(path string) (Config, error) {

	var conf Config

	if path == "" {
		return conf, errInvalidConfigPath
	}

	if err := loadFile(path, &conf); err != nil {
		return conf, err
	}

	return conf, nil
}

func loadFile(path string, source interface{}) error {
	content, err := ioutil.ReadFile(path)
	if err != nil {
		return err
	}

	return json.Unmarshal(content, source)
}
