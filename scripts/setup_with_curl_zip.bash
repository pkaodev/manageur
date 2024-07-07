#!/bin/bash

_MANAGEUR="${HOME}/_manageur"
ZIP_URL="https://github.com/pkaodev/Manageur/archive/refs/heads/main.zip"
TMP_DIR="tmp_manageur_dir"
TMP_ZIP="tmp_manageur_zip.zip"
BASHRC="${HOME}/.bashrc"
BASHRC_SOURCE="source ${_MANAGEUR}/src/_home/bashrc"

cleanup() {
    rm -rf "${TMP_DIR}" "${TMP_ZIP}"
}

trap cleanup EXIT

if ! grep -qF "${BASHRC_SOURCE}" "${BASHRC}"; then
    echo "${BASHRC_SOURCE}" >> "${BASHRC}"
fi

curl -sL "${ZIP_URL}" -o "${TMP_ZIP}"
unzip -q "${TMP_ZIP}" -d "${TMP_DIR}"

rm -rf "${_MANAGEUR}"
mkdir -p "${_MANAGEUR}"
mv "${TMP_DIR}/Manageur-main/"* "${_MANAGEUR}/"

(
    cd "${_MANAGEUR}" || exit

    python3 -m venv .venv

	_python="${_MANAGEUR}/.venv/bin/python"

    . .venv/bin/activate

    pip3 install -r requirements.txt

   $_python src/main.py &
)

cleanup
