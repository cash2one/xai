

#calss header
class _LABIAL():
	def __init__(self,): 
		self.name = "LABIAL"
		self.definitions = [u'Labial sounds are consonant sounds made with the two lips: ', u'relating to the lips: ', u'relating to the folds on the outside of the female sex organs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
