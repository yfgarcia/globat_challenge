DATA_Q = """
	with qry1 as (
		select 
			dp.department,
			he.department_id,
			j.job,
			he.job_id,
			count(he.id) as Q1
		from public.departments dp
		inner join public.hired_employees he on dp.id = he.department_id
		inner join public.jobs j on he.job_id = j.id 
		where substring(he.datetime,1,4) = '2021'
			and right(substring(he.datetime,1,7),2) in ('01','02','03')
		group by 1,2,3,4
	), qry2 as (
		select 
			dp.department,
			he.department_id,
			j.job,
			he.job_id,
			count(he.id) as Q2
		from public.departments dp
		inner join public.hired_employees he on dp.id = he.department_id
		inner join public.jobs j on he.job_id = j.id 
		where substring(he.datetime,1,4) = '2021'
			and right(substring(he.datetime,1,7),2) in ('04','05','06')
		group by 1,2,3,4
	), qry3 as (
		select 
			dp.department,
			he.department_id,
			j.job,
			he.job_id,
			count(he.id) as Q3
		from public.departments dp
		inner join public.hired_employees he on dp.id = he.department_id
		inner join public.jobs j on he.job_id = j.id 
		where substring(he.datetime,1,4) = '2021'
			and right(substring(he.datetime,1,7),2) in ('07','08','09')
		group by 1,2,3,4
	) , qry4 as (
		select 
			dp.department,
			he.department_id,
			j.job,
			he.job_id,
			count(he.id) as Q4
		from public.departments dp
		inner join public.hired_employees he on dp.id = he.department_id
		inner join public.jobs j on he.job_id = j.id 
		where substring(he.datetime,1,4) = '2021'
			and right(substring(he.datetime,1,7),2) in ('10','11','12')
		group by 1,2,3,4
	) 
		select 
			coalesce(qry1.department,
						qry2.department,
						qry3.department,
						qry4.department) as department ,
			coalesce(qry1.job,
						qry2.job,
						qry3.job,
						qry4.job) as job ,
			Q1,
			Q2,
			Q3,
			Q4
		from qry1 
		left join qry2 on qry1.department_id = qry2.department_id and qry1.job_id = qry2.job_id
		left join qry3 on qry1.department_id = qry3.department_id and qry1.job_id = qry3.job_id
		left join qry4 on qry1.department_id = qry4.department_id and qry1.job_id = qry4.job_id
		order by 1,2
"""

LIST_ID = """
	select 
		he.department_id,
		d.department,
		count(he.id) as hired
	from public.hired_employees he 
	join public.departments d on HE.department_id = d.id 
	join public.jobs j on he.job_id = j.id  
	where substring(he.datetime,1,4) = '2021'
	group by 1,2
	order by 3 desc
"""