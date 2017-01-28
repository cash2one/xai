

#calss header
class _UNPALATABLE():
	def __init__(self,): 
		self.name = "UNPALATABLE"
		self.definitions = [u'An unpalatable fact or idea is unpleasant or shocking and therefore difficult to accept: ', u'Unpalatable food is unpleasant to taste or eat.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
