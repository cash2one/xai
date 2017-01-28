

#calss header
class _RESPONSIBLE():
	def __init__(self,): 
		self.name = "RESPONSIBLE"
		self.definitions = [u'to have control and authority over something or someone and the duty of taking care of it, him, or her: ', u'to be controlled by someone or something: ', u'to be the person who caused something to happen, especially something bad: ', u'to blame someone or something: ', u'to be in control of yourself so that you can fairly be blamed for your bad actions: ', u'having good judgment and the ability to act correctly and make decisions on your own: ', u'A responsible job or position involves making important decisions or doing important things.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
