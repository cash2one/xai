

#calss header
class _CLINICALLY():
	def __init__(self,): 
		self.name = "CLINICALLY"
		self.definitions = [u'according to medical science and examination of patients: ', u'relating to the results of clinical tests or experiments: ', u'in a way that lacks emotion or sympathy: ', u'in a way that lacks warmth or comfort ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
