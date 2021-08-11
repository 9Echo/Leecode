## SQL练习

1. 查询出每门课程的成绩都大于80的学生姓名

   ```sql
   SELECT S.name
   FROM Student S
   GROUP BY S.name
   Having MIN(S.score)>=80
   ```

2. 计算每个人的总成绩并排名（姓名，总成绩）

   ```sql
   select name, sum(score) as allscore from stu_score group by name order by allscore
   ```

3. 计算每个人的总成绩并排名（姓名，学号，总成绩）

   ```sql
   select stuid, name, sum(score) as allscore from stu_score group by stuid, name order by allscore
   ```

4. 计算每个人单科的最高成绩

   ```sql
   select t1.stuid, t1.name, t1.subject, t1.score from stuscore t1,
   (
   select stuid, max(score) as maxscore from stuscore group by stuid
   )t2
   where t1.stuid = t2.stuid and t1.score 
   ```

   

