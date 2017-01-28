

#calss header
class _MYOPIC():
	def __init__(self,): 
		self.name = "MYOPIC"
		self.definitions = [u'not able to see clearly things that are far away', u'unable to understand a situation or the way actions will affect it in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
