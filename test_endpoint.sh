#!/bin/bash

emergency() {
    set +x

    if [ "$1" == "STAGE" ];
    then
        ENV_ENDPOINT="https://alura-product-recommendations-stage.sorocaba.sp.gov.br/emergency/"
    else
        ENV_ENDPOINT="http://alura-product-recommendations-local.sorocaba.sp.gov.br:8000/emergency/"
    fi

    # TODO use another geom format: WKT
    # -F "geom=SRID=31983;POINT (334084.6591700006 7396449.925171347)" \

    curl -i -X POST -F "photo01=@/home/jecampos/universal/projects/pms/defesa_civil/images/flood01.jpg" \
         -F "nivel_agua=ALTO" \
         -F "data_pedido_ajuda=2024-10-04T12:37:45.983520-03:00" \
         -F "nome_completo=Test cUrl 01" \
         -F "cpf=17856324980" \
         -F "telefone01=15991234470" \
         -F "telefone02=" \
         -F "endereco_ajuda=Rua Test cUrl 01" \
         -F "complemento=158" \
         -F "pedido_relatado=Help! Flood!!" \
         -F "adultos=1" \
         -F "criancas=0" \
         -F "idosos=0" \
         -F "deficientes=0" \
         -F "acamados=0" \
         -F "animais=0" \
         -F "beira_corrego=false" \
         $ENV_ENDPOINT
}

generic_get() {
    URL="$BASE_ENDPOINT/$1"

    # set -x
    curl -s -H 'Accept-Language: pt-br' -H "Accept: application/json" -u $CREDENTIALS -X GET $URL
}

user_list() {
    generic_get "users/"
}

user_create() {
    curl -s -X POST "$BASE_ENDPOINT/users/?name=$1"
}

API_USER="$(cat .env | grep API_USER | cut -d = -f2 | sed -n '1,1p')"
API_PASS="$(cat .env | grep API_PASS | cut -d = -f2 | sed -n '1,1p')"
CREDENTIALS="$API_USER:$API_PASS"

case $2 in
    "LOCAL") BASE_ENDPOINT="http://alura-product-recommendations-local.sorocaba.sp.gov.br:8000";;
    "DEV") BASE_ENDPOINT="https://alura-product-recommendations-dev.sorocaba.sp.gov.br";;
    "STAGE") BASE_ENDPOINT="https://alura-product-recommendations-stage.sorocaba.sp.gov.br";;
    "PROD") BASE_ENDPOINT="https://alura-product-recommendations.sorocaba.sp.gov.br";;
    *) 
        BASE_ENDPOINT="http://localhost:8000"
        # echo "USAGE: [LOCAL | DEV | STAGE | PROD]. $2 *NOT* found!!"
        # echo "USING $BASE_ENDPOINT by default."
        ;;
esac

case $1 in
    "gen_get") generic_get $3;;
    "user_list") user_list;;
    "user_create") user_create $3;;
    *) echo "USAGE: [emergency | guideline | flood | auth | help] [LOCAL | DEV | STAGE | PROD]. $1 *NOT* found!!"
esac
