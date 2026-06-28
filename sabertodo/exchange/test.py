from rest_framework import status
from rest_framework.test import APITestCase

from student.models import Student
from rules.models import Rule
from exchange.models import Exchange


class ExchangeAPITest(APITestCase):

    def setUp(self):
        self.student = Student.objects.create(
            Name="小明",
            Phone="+8613812345678",
            Score=500,
            Energy=20,
            PetFood=10
        )

        self.rule = Rule.objects.create(
            Name="兑换30分钟游戏",
            NeedScore=100,
            RewardEnergy=20,
            RewardPetFood=5
        )

        self.exchange = Exchange.objects.create(
            Student=self.student,
            Rule=self.rule,
            CostScore=100,
            GainEnergy=20,
            GainPetFood=5
        )

    def test_list_exchange(self):
        """查询兑换记录"""

        response = self.client.get("/api/exchange/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_detail_exchange(self):
        """查询详情"""

        response = self.client.get(
            f"/api/exchange/{self.exchange.id}/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["CostScore"], 100)

    def test_create_exchange(self):
        """新增兑换"""

        data = {
            "Student": self.student.id,
            "Rule": self.rule.id,
            "CostScore": 200,
            "GainEnergy": 30,
            "GainPetFood": 10
        }

        response = self.client.post(
            "/api/exchange/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Exchange.objects.count(),
            2
        )

    def test_update_exchange(self):
        """修改兑换"""

        data = {
            "Student": self.student.id,
            "Rule": self.rule.id,
            "CostScore": 150,
            "GainEnergy": 50,
            "GainPetFood": 20
        }

        response = self.client.put(
            f"/api/exchange/{self.exchange.id}/",
            data,
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.exchange.refresh_from_db()

        self.assertEqual(self.exchange.CostScore, 150)
        self.assertEqual(self.exchange.GainEnergy, 50)

    def test_patch_exchange(self):
        """局部更新"""

        response = self.client.patch(
            f"/api/exchange/{self.exchange.id}/",
            {
                "GainEnergy": 99
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.exchange.refresh_from_db()

        self.assertEqual(
            self.exchange.GainEnergy,
            99
        )

    def test_delete_exchange(self):
        """删除"""

        response = self.client.delete(
            f"/api/exchange/{self.exchange.id}/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Exchange.objects.count(),
            0
        )