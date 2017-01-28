

#calss header
class _TRAUMATIC():
	def __init__(self,): 
		self.name = "TRAUMATIC"
		self.definitions = [u'If an experience is traumatic, it causes you severe emotional shock and upset: ', u'frightening and causing worry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
