# Azure CLI context wrapper — uses the active jig azure context
az() {
    if [[ -f ~/.jig/azure/active ]]; then
        AZURE_CONFIG_DIR="$HOME/.jig/azure/contexts/$(cat ~/.jig/azure/active)" command az "$@"
    else
        command az "$@"
    fi
}
