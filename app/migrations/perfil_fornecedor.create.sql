create table perfil_fornecedor
(
	id_perfil int not null,
	id_fornecedor int not null,
	constraint fk_perfil_perfil_fornecedor
		foreign key(id_perfil)
		references perfil(id),
	constraint fk_fornecedor_perfil_fornecedor
		foreign key(id_fornecedor)
		references fornecedor(id)
);
