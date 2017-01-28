

#calss header
class _COMPOUND():
	def __init__(self,): 
		self.name = "COMPOUND"
		self.definitions = [u'consisting of two or more parts', u'used to refer to a system of paying interest in which interest is paid both on the original amount of money invested (= given to companies hoping to get more back) or borrowed and on the interest that has collected over a period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
