

#calss header
class _INSUBORDINATE():
	def __init__(self,): 
		self.name = "INSUBORDINATE"
		self.definitions = [u'(of a person) not willing to obey orders from people in authority, or (of actions and speech, etc.) showing that you are not willing to obey orders: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
