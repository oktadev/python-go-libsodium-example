package main

import (
	"fmt"
	"io/ioutil"

	"golang.org/x/crypto/nacl/secretbox"
)

var SecretKey [32]byte

func GetKey() {
	sk, _ := ioutil.ReadFile("key_secret")
	copy(SecretKey[:], sk)
}

func Decrypt() {
	enc, _ := ioutil.ReadFile("message.sec")
	var nonce [24]byte
	copy(nonce[:], enc[:24])
	crypto := enc[24:]
	message, _ := secretbox.Open(nil, crypto, &nonce, &SecretKey)
	fmt.Println(string(message))
}

func main() {
	GetKey()
	Decrypt()
}
