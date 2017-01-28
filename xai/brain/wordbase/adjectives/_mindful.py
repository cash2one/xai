

#calss header
class _MINDFUL():
	def __init__(self,): 
		self.name = "MINDFUL"
		self.definitions = [u'careful not to forget about something: ', u'deliberately aware of your body, mind, and feelings in the present moment, in order to create a feeling of calm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
