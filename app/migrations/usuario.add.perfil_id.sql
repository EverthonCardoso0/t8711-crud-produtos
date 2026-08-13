alter table usuario add column perfil_id integer not null;
alter table usuario add constraint fk_perfil_usuario foreign key(perfil_id) references perfil(id);
