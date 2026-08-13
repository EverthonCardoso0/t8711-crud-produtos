create table fornecedor_categoria
(
	id_fornecedor int not null,
	id_categoria int not null,
	constraint fk_fornecedor_fornecedor_categoria
		foreign key(id_fornecedor)
		references fornecedor(id),
	constraint fk_categoria_fornecedor_categoria
		foreign key(id_categoria)
		references categoria(id)
);
