

#calss header
class _TIRED():
	def __init__(self,): 
		self.name = "TIRED"
		self.definitions = [u'in need of rest or sleep: ', u'used to describe people, ideas, or subjects that are not interesting because they are very familiar: ', u'to be bored with an activity or person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
