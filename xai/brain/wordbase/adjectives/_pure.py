

#calss header
class _PURE():
	def __init__(self,): 
		self.name = "PURE"
		self.definitions = [u'not mixed with anything else: ', u'A pure colour is not mixed with any other colour: ', u'A pure sound is clear and perfect: ', u'clean and free from harmful substances: ', u'complete; only: ', u'used to refer to an area of study that is studied only for the purpose of developing theories about it, not for the purpose of using those theories in a practical way: ', u'used after a noun to mean "and nothing else": ', u'behaving in a way that is morally good, especially in things related to sex: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
