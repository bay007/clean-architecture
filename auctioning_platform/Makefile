# order of libs is meaningful. First, we install libs without internal dependencies that other libs depend on.
libs := foundation auctions shipping db_infrastructure web_app_models auctions_infrastructure shipping_infrastructure customer_relationship payments processes main web_app

define install_dev
	pip install -e $(1)

endef

.PHONY: dev
dev:
	pip install -r requirements.txt -r requirements-dev.txt
	$(foreach lib,$(libs),$(call install_dev,$(lib)))

.PHONY: freeze-deps
freeze-deps:
	pip install pip-tools==4.4.1
	pip-compile --output-file=requirements.txt $(foreach lib,$(libs), ./$(lib)/requirements.txt ./$(lib)/requirements-dev.txt)
