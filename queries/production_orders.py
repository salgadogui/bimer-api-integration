production_orders = \
    """
    SELECT
        MAX(EMP.NmEmpresa) As NmEmpresa,
        PP.CdChamada,
        PP.NmProduto,
        COUNT(DISTINCT OSEI.IdOrdemServicoEquipamentoItem) AS QtOSEmitidas,
        SUM(DISTINCT PVI.QtPedida) AS QtPedidaPV,
        COALESCE(SUM(DISTINCT PVI.QtAtendida), 0) AS QtAtendidaPV,
        (SUM(DISTINCT PVI.QtPedida) - COALESCE(SUM(DISTINCT PVI.QtAtendida), 0)) AS QtRestantePV,
        (COALESCE(SUM(DISTINCT PVI.QtAtendida), 0) / SUM(DISTINCT PVI.QtPedida)) AS PercentualConcluidoPV,
        STRING_AGG(LTRIM(RTRIM(CONVERT(varchar(max), OS.CdChamada))), ',') AS CdOsEmitidas,
        MAX(OS.DtLimiteServico) As DtLimiteServico

    FROM 
        PedidoDeVendaItem AS PVI
        JOIN vw_ProdutoPrincipal AS PP ON               PP.IdProduto = PVI.IdProduto
        JOIN Equipamento AS EQ ON                       EQ.IdProduto = PVI.IdProduto
        JOIN OrdemServicoEquipamento AS OSE ON          OSE.IdEquipamento = EQ.IdEquipamento
        JOIN OrdemServicoEquipamentoItem AS OSEI ON     OSEI.IdOrdemServicoEquipamento = OSE.IdOrdemServicoEquipamento
        JOIN OrdemServico AS OS ON                      OS.IdOrdemServico = OSE.IdOrdemServico
        JOIN EmpresaERP AS EMP ON                       EMP.CdEmpresa = OS.CdEmpresa
        
    GROUP BY
        PP.CdChamada, 
        PP.NmProduto
    """