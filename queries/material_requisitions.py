material_requisitions = \
    """
        SELECT TOP 6000
            CC.CdChamada AS CdChamadaCC,
            RMI.StRequisicaoMaterialItem,
            CC.NmCentroDeCusto,
            RM.CdChamada AS CdChamadaRM,
            PP.NmProduto AS NmProdutoInsumo,
            PP.CdChamada AS CdChamadaInsumo,
            RM.DtRequisicaoMaterial,
            U.NmUnidade,
            RMI.QtRequerida,
            COALESCE(RMIB.QtAtendida, 0) AS QtAtendida,
            (RMI.QtRequerida - COALESCE(RMIB.QtAtendida, 0)) AS QtRestante,
            US.NmUsuario,
            S.NmSetor AS NmSetorRequisitado,
            CC.StAtivo,
            OS.StOS,
            OS.CdChamada AS CdChamadaOS,
            COALESCE(RM.NmEntidadeOrigem, 'BimerUP') AS NmEntidadeOrigem,
            (
                SELECT TOP 1 ES.QtEstoque 
                FROM EstoqueSetor AS ES 
                WHERE ES.IdProduto = PP.IdProduto 
                ORDER BY ES.DtReferencia DESC
            ) AS QtItemEstoque

        FROM RequisicaoMaterial AS RM

        JOIN RequisicaoMaterialItem AS RMI                   ON RMI.IdRequisicaoMaterial = RM.IdRequisicaoMaterial
        LEFT JOIN RequisicaoMaterialItemBaixa AS RMIB        ON RMIB.IdRequisicaoMaterialItem = RMI.IdRequisicaoMaterialItem
        JOIN vw_ProdutoPrincipal AS PP                       ON PP.IdProduto = RMI.IdProduto
        JOIN CentroDeCusto AS CC                             ON CC.IdCentroDeCusto = RM.IdCentroDeCusto
        LEFT JOIN OrdemServico AS OS                         ON OS.CdChamada = RIGHT(CONVERT(VARCHAR(MAX), RM.DsObservacao), 6)
        JOIN Setor AS S                                      ON S.IdSetor = RM.IdSetorRequisitado
        JOIN Usuario AS US                                   ON US.IdUsuario = RM.IdUsuario
        JOIN Unidade AS U                                    ON U.IdUnidade = RMI.IdUnidade
    
        WHERE S.NmSetor <> 'PRODUCAO'

        ORDER BY RM.DtRequisicaoMaterial DESC
    """
