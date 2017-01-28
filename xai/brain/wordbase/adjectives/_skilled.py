

#calss header
class _SKILLED():
	def __init__(self,): 
		self.name = "SKILLED"
		self.definitions = [u'having the abilities needed to do an activity or job well: ', u'Skilled work needs someone who has had special training to do it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
