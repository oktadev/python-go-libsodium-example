package main

import (
	"encoding/hex"
	"fmt"
	"io/ioutil"

	"golang.org/x/crypto/nacl/box"
)

var PublicKey [32]byte
var SecretKey [32]byte

func GetKeys() {
	sk, _ := ioutil.ReadFile("key_bob_sk")
	keysk, _ := hex.DecodeString(string(sk))
	copy(SecretKey[:], keysk)
	pk, _ := ioutil.ReadFile("key_alice_pk")
	keypk, _ := hex.DecodeString(string(pk))
	copy(PublicKey[:], keypk)
}

func Decrypt() {
	enc, _ := ioutil.ReadFile("message.enc")
	var nonce [24]byte
	copy(nonce[:], enc[:24])
	crypto := enc[24:]
	message, _ := box.Open(nil, crypto, &nonce, &PublicKey, &SecretKey)
	fmt.Println(string(message))
}

func main() {
	GetKeys()
	Decrypt()
}
