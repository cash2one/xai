

#calss header
class _BASIC():
	def __init__(self,): 
		self.name = "BASIC"
		self.definitions = [u'simple and not complicated, so able to provide the base or starting point from which something can develop: ', u'boring and not unusual or surprising in any way: ', u'what a person earns before other amounts of money, such as payments for working extra hours, are added: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
